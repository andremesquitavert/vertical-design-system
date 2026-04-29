# Changelog — Vertical Design System

Formato: `[versão] — YYYY-MM-DD — descrição`

---

## [1.1.0] — 2026-04-29

### Adicionado
- Dark theme completo (`tokens/dark.css`) via seletor `[data-theme="dark"]`
  — cobre todos os tokens: layout, tipografia, accent, status, prioridade, feedback, roxo e sombras
- Tokens novos em `variables.css`: `--surface-subtle`, `--surface-muted`, `--surface-hover`, `--border-subtle`, `--scrollbar-thumb`

### Modificado
- Todos os valores hardcoded nos componentes substituídos pelos novos tokens
  — `table` (thead, count pill, hover), `drawer` (footer, desc-box), `badge` (neutral),
    `timeline` (dot pending, line pending), `pa-card` (body text), `utilities` (scrollbar)
- `scripts/build.py` agora inclui `tokens/dark.css` no bundle

---

## [1.0.0] — 2026-04-29

### Adicionado
- Design tokens completos (`tokens/variables.css`): paleta, tipografia, espaçamentos, sombras, tokens de status e prioridade
- Componente `reset` — box-sizing, fonte base (DM Sans), antialiasing
- Componente `layout` — `vds-app`, `vds-main`, `vds-content`
- Componente `sidebar` — colapsável, logo, nav, badges, toggle
- Componente `topbar` — breadcrumb, relógio, seletor de unidade, avatar, role pill
- Componente `kpi` — grid de métricas com `--kpi-color`, seleção por filtro
- Componente `table` — `vds-table-card`, busca inline, empty state, células tipadas
- Componente `badge` — status (aberta/aceita/aguardando/analise/concluida/reprovada), prioridade (alta/media/baixa), neutro
- Componente `button` — 6 variantes (primary/outline/ghost/danger/success/purple), 3 tamanhos, estado disabled
- Componente `alert` — info/warn/success/error
- Componente `form` — `vds-field`, `vds-form-group`, labels com required/hint, erro, checkbox row
- Componente `drawer` — overlay, painel deslizante, header/body/footer, info-grid, desc-box
- Componente `timeline` — passos done/current/pending com linhas conectoras
- Componente `pa-card` — card de plano de ação / nota estruturada em roxo
- Componente `toast` — notificações temporárias (success/warn/error/info)
- Componente `utilities` — animações, spinner, classes de texto, scrollbar customizada
- Script `scripts/build.py` — gera `dist/vertical-design-system.css`
- Docs `docs/index.html` — guia visual interativo de todos os componentes

### Base
Originado do design do Portal Qualidade (Grupo Vertical Saúde, 2026),
que por sua vez foi derivado do Portal Logística.

---

<!-- Template para próximas versões:

## [1.x.0] — YYYY-MM-DD

### Adicionado
- ...

### Modificado
- ...

### Corrigido
- ...

### Removido
- ...

-->
