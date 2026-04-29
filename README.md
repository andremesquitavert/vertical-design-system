# Vertical Design System

Sistema de design compartilhado do Grupo Vertical Saúde — Governança de TI.

Tipografia: **DM Sans** · Ícones: **Font Awesome 6.5** · Prefixo: **`vds-`**

---

## Estrutura

```
vertical-design-system/
├── tokens/
│   └── variables.css          ← design tokens (cores, espaçamentos, sombras)
├── components/
│   ├── reset.css
│   ├── layout.css             ← vds-app, vds-main, vds-content
│   ├── sidebar.css
│   ├── topbar.css
│   ├── kpi.css
│   ├── table.css
│   ├── badge.css
│   ├── button.css
│   ├── alert.css
│   ├── form.css
│   ├── drawer.css
│   ├── timeline.css
│   ├── pa-card.css
│   ├── toast.css
│   └── utilities.css
├── dist/
│   └── vertical-design-system.css   ← arquivo único compilado (gerado)
├── docs/
│   └── index.html                   ← guia visual interativo
└── scripts/
    └── build.py                     ← gera dist/ a partir de components/
```

---

## Uso em um projeto

### 1. Adicionar como submodule

```bash
git submodule add https://github.com/andremesquitavert/vertical-design-system static/vds
git submodule update --init
```

### 2. Importar no HTML base

```html
<head>
  <!-- Tipografia -->
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">

  <!-- Ícones -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

  <!-- Design System (arquivo único compilado) -->
  <link rel="stylesheet" href="/static/vds/dist/vertical-design-system.css">

  <!-- CSS específico do projeto (overrides e extensões) -->
  <link rel="stylesheet" href="/static/css/meu-projeto.css">
</head>
```

### 3. Estrutura HTML mínima

```html
<div class="vds-app">

  <nav class="vds-sidebar" id="js-sidebar">
    <div class="vds-sidebar__logo">
      <div class="vds-sidebar__mark"><i class="fas fa-icon"></i></div>
      <div class="vds-sidebar__text">
        <div class="vds-sidebar__name">Nome do Portal</div>
        <div class="vds-sidebar__sub">Vertical Saúde · GovTI</div>
      </div>
    </div>
    <nav class="vds-sidebar__nav">
      <a href="/" class="vds-sidebar__item is-active">
        <i class="fas fa-home vds-sidebar__icon"></i>
        <span>Início</span>
      </a>
    </nav>
  </nav>

  <div class="vds-main">
    <header class="vds-topbar">
      <div class="vds-breadcrumb">
        <span>Portal</span>
        <span class="vds-breadcrumb__sep">›</span>
        <span class="vds-breadcrumb__current">Página</span>
      </div>
    </header>
    <main class="vds-content">
      <!-- conteúdo aqui -->
    </main>
  </div>

</div>
```

### 4. Customizar tokens do projeto

```css
/* static/css/meu-projeto.css */
:root {
  --accent:      #10b981;   /* cor principal diferente */
  --accent-dark: #059669;
}
```

---

## Atualizar o submodule para a versão mais recente

```bash
git submodule update --remote static/vds
git add static/vds
git commit -m "chore: atualiza vertical-design-system"
```

---

## Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo completo.

**Resumo:** abra uma branch → edite `components/` → rode `python scripts/build.py` → abra PR.
