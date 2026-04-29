"""
Build — Vertical Design System
===============================
Concatena tokens/ + components/ → dist/vertical-design-system.css

Uso:
    python scripts/build.py
"""
from pathlib import Path
from datetime import datetime

ROOT       = Path(__file__).parent.parent
TOKENS     = ROOT / "tokens"
COMPONENTS = ROOT / "components"
DIST       = ROOT / "dist"
OUTPUT     = DIST / "vertical-design-system.css"

# Ordem de importação — altere se adicionar novos componentes
ORDER = [
    TOKENS     / "variables.css",
    TOKENS     / "dark.css",
    COMPONENTS / "reset.css",
    COMPONENTS / "layout.css",
    COMPONENTS / "sidebar.css",
    COMPONENTS / "topbar.css",
    COMPONENTS / "kpi.css",
    COMPONENTS / "table.css",
    COMPONENTS / "badge.css",
    COMPONENTS / "button.css",
    COMPONENTS / "alert.css",
    COMPONENTS / "form.css",
    COMPONENTS / "drawer.css",
    COMPONENTS / "timeline.css",
    COMPONENTS / "pa-card.css",
    COMPONENTS / "toast.css",
    COMPONENTS / "utilities.css",
]

HEADER = f"""\
/*
 * ============================================================
 *  VERTICAL DESIGN SYSTEM
 *  Grupo Vertical Saúde · Governança de TI
 * ============================================================
 *  Gerado por: scripts/build.py
 *  Data:       {datetime.now().strftime('%Y-%m-%d %H:%M')}
 *
 *  NÃO edite este arquivo diretamente.
 *  Edite os arquivos em tokens/ ou components/ e rode o build.
 *
 *  Imports obrigatórios no HTML:
 *    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
 *    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
 *    <link rel="stylesheet" href="vertical-design-system.css">
 * ============================================================
 */

"""


def build() -> None:
    DIST.mkdir(exist_ok=True)
    partes = [HEADER]

    for path in ORDER:
        if not path.exists():
            print(f"  [AVISO] {path.name} não encontrado — pulando")
            continue
        conteudo = path.read_text(encoding="utf-8").strip()
        partes.append(conteudo + "\n")
        print(f"  ok {path.relative_to(ROOT)}")

    # Componentes extras não listados em ORDER (descoberta automática)
    listados = set(ORDER)
    for extra in sorted(COMPONENTS.glob("*.css")):
        if extra not in listados:
            conteudo = extra.read_text(encoding="utf-8").strip()
            partes.append(f"\n/* ── {extra.stem} (extra) ── */\n" + conteudo + "\n")
            print(f"  ok {extra.relative_to(ROOT)}  [descoberto automaticamente]")

    OUTPUT.write_text("\n\n".join(partes), encoding="utf-8")
    size = OUTPUT.stat().st_size / 1024
    print(f"\n>> {OUTPUT.relative_to(ROOT)}  ({size:.1f} KB)")


if __name__ == "__main__":
    print("=== VDS Build ===")
    build()
    print("=== Concluído ===")
