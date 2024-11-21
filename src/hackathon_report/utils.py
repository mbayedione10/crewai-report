from pathlib import Path
from datetime import datetime

def save_report(content):
    """Sauvegarder le rapport dans un fichier."""
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)
    report_path = output_dir / f'rapport_mentorat_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Rapport sauvegardé dans : {report_path}")
