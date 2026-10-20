import urllib.request
import json
import os
import sys

SYMBOLS = {
    'IBOV': '^BVSP',
    'SPX': '^GSPC',
    'BRENT': 'BZ=F',
    'GOLD': 'GC=F'
}

def fetch_market_data():
    cache = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for key, sym in SYMBOLS.items():
        url = f'https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=1y'
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                res = data['chart']['result'][0]
                meta = res['meta']
                price = meta['regularMarketPrice']
                prev = meta.get('chartPreviousClose') or meta.get('previousClose')
                chg = ((price - prev) / prev) * 100 if prev else 0.0

                timestamps = res.get('timestamp', [])
                quotes = res['indicators']['quote'][0]
                closes = quotes.get('close', [])

                points = []
                for t, c in zip(timestamps, closes):
                    if c is not None:
                        points.append({'t': t, 'c': round(c, 2)})

                cache[key] = {
                    'price': round(price, 2),
                    'pctChange': round(chg, 2),
                    'points': points
                }
                print(f"[{key}] Atualizado com sucesso: {price:.2f} ({chg:+.2f}%)")
        except Exception as e:
            print(f"[{key}] Erro ao buscar cotação: {e}", file=sys.stderr)

    if len(cache) == len(SYMBOLS):
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'market_cache.json')
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(cache, f, separators=(',', ':'))
        print("market_cache.json gravado com sucesso.")
    else:
        print("Aviso: nem todos os ativos retornaram dados. Mantendo cache anterior para evitar corrupção.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    fetch_market_data()
