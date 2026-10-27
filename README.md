[README.md](https://github.com/user-attachments/files/34038967/README.md)
# GAMA – Site Institucional

Site oficial do **Grupo de Análise Macroeconômica Aplicada** da PUC-Rio.

🔗 [gmagno778.github.io/gama-pucrio](https://gmagno778.github.io/gama-pucrio)

---

## Estrutura de arquivos

```
gama-pucrio/
├── index.html          # Arquivo principal do site
├── 1.png               # Logo do GAMA
├── logo_puc.png        # Logo da PUC-Rio
├── cartas/             # PDFs das Cartas de Conjuntura
└── relatorios/         # PDFs dos Relatórios Analíticos
```

---

## Como atualizar o site

### Adicionar uma nova Carta de Conjuntura
1. Suba o PDF na pasta `cartas/` via **Add file → Upload files**
2. No `index.html`, localize a seção `cartas-grid`
3. A carta mais recente deve ter a classe `carta-card carta-destaque` com o badge *"Edição mais recente"*
4. A carta anterior perde o badge mas mantém a classe `carta-destaque`
5. Cartas mais antigas usam apenas a classe `carta-card`

### Adicionar um novo Relatório
1. Suba o PDF na pasta `relatorios/`
2. No `index.html`, localize a seção `relatorios-list`
3. Cole um novo bloco `<a class="relatorio-item">` incrementando o número

### Atualizar a equipe
- Busque pelo nome do membro no `index.html`
- Cada diretoria tem seu bloco identificado por `diretoria-label`
- Membros são ordenados alfabeticamente, com diretores no topo

### Atualizar o Processo Seletivo
- Busque por `id="ps"` no `index.html`
- O link do formulário está no atributo `href` do botão de inscrição

---

## Cores do site

| Variável | Hex | Uso |
|---|---|---|
| `--navy` | `#001b58` | Azul principal |
| `--navy-deep` | `#00062e` | Fundo hero e footer |
| `--off-white` | `#f4f2f3` | Fundo seções claras |
| `--slate` | `#303a44` | Fundo seção equipe |
| `--accent` | `#c9a84c` | Dourado — destaques |

Todas as cores ficam no topo do `index.html`, dentro de `:root { }`.

---

## Hospedagem

O site é estático e está hospedado via **GitHub Pages** (branch `main`, raiz `/`). Qualquer commit na branch `main` atualiza o site automaticamente em segundos.

---

## Tecnologias

- HTML5 + CSS3 + JavaScript puro (sem frameworks)
- Fontes: Playfair Display e DM Sans via Google Fonts
- Sem dependências externas além das fontes

---

## Contato técnico

Dúvidas sobre o código: falar com o presidente da gestão que criou o site ou abrir uma *issue* no repositório.
