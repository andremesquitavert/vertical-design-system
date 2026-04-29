# Contribuindo com o Vertical Design System

## Fluxo de contribuição

Qualquer projeto pode propor novos componentes ou mudanças em existentes.
O processo é simples — basta criar uma branch e abrir um PR.

```
1. git checkout -b feat/nome-do-componente
2. Edite ou crie o arquivo em components/ ou tokens/
3. Documente no docs/index.html
4. Execute: python scripts/build.py
5. Abra um PR descrevendo o componente e qual projeto o motivou
```

---

## Onde cada coisa vai

| Situação | Arquivo |
|---|---|
| Nova variável de cor, espaçamento ou sombra | `tokens/variables.css` |
| Novo componente reutilizável (2+ projetos) | `components/nome.css` (novo arquivo) |
| Nova variante de componente existente | `components/nome.css` (adicionar modificador) |
| Componente específico de um projeto | CSS do próprio projeto — **não vai no DS** |
| Override de token por projeto | CSS do próprio projeto — `--accent: #outra-cor;` |

---

## Convenções obrigatórias

### Prefixo `vds-`
Toda classe do design system começa com `vds-`.
```css
/* ✓ correto */
.vds-card { ... }
.vds-card--highlighted { ... }

/* ✗ errado */
.card { ... }
.my-card { ... }
```

### BEM adaptado
```
.vds-[componente]               ← bloco
.vds-[componente]__[elemento]   ← elemento interno
.vds-[componente]--[variante]   ← modificador / variante
```

### Estados dinâmicos
Use classes `is-` para estados controlados por JavaScript.
Nunca estilize IDs `js-*` — eles são exclusivos do JavaScript.
```css
.vds-sidebar.is-collapsed { ... }   /* ✓ */
#js-sidebar { ... }                 /* ✗ */
```

### CSS custom properties para valores variáveis
Prefira variáveis a valores fixos sempre que um dado puder mudar por projeto ou contexto.
```css
/* ✓ */
color: var(--accent);

/* ✗ */
color: #2563eb;
```

### Sem `!important`
Se precisou de `!important`, o componente precisa ser refatorado.

---

## Adicionando um novo componente

1. Crie `components/meu-componente.css`
2. Siga a estrutura de comentário padrão:
```css
/* ── Nome do Componente ─────────────────────────────────────── */

.vds-meu-componente { ... }
.vds-meu-componente--variante { ... }
.vds-meu-componente__elemento { ... }
```
3. Adicione o arquivo na lista `ORDER` em `scripts/build.py`
4. Documente no `docs/index.html` com exemplo de uso em HTML
5. Rode `python scripts/build.py` para gerar o `dist/`
6. Abra o PR

---

## Modificando um componente existente

- Prefira **adicionar modificadores** a alterar o comportamento padrão
- Se a mudança quebra projetos existentes, discuta no PR antes de fazer merge
- Registre a mudança no `CHANGELOG.md`

---

## Checklist do PR

- [ ] Segue o prefixo `vds-` e as convenções BEM
- [ ] Usa variáveis CSS (`var(--...)`) em vez de valores fixos
- [ ] Sem `!important`
- [ ] Documentado no `docs/index.html`
- [ ] `python scripts/build.py` rodou sem erros
- [ ] `CHANGELOG.md` atualizado
