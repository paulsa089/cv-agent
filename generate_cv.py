import os
from jinja2 import Environment, FileSystemLoader
import subprocess

# Pfade definieren
TEMPLATE_DIR = '.'  # Das Verzeichnis, in dem das LaTeX-Template liegt
TEMPLATE_FILE = 'cv_template.tex'

# Beispiel-Daten für den Lebenslauf
cv_data = {
    'job_title': 'Finanzbuchhalter',
    'name': 'Luc Manns',
    'email': 'luc.manns@avl-recruiting.de',
    'phone': '+49 151 46330868',
    'salary': '48.000 € brutto/Jahr',
    'availability': 'Kurzfristig, mit 1 Monat Kündigungsfrist',
    'birth_year': '1996',
    'location': 'Berlin (flexibel innerhalb des Stadtgebiets und Umland)',
    'marital_status': 'Ledig',
    'nationality': 'Deutsch',
    'career_goal': 'Digitalaffiner Finanzbuchhalter mit drei Jahren Erfahrung in der operativen Buchhaltung, insbesondere in der Rechnungsbearbeitung und Monatsabschlusserstellung. Ich suche im Raum Berlin eine Position in einem modernen, prozessorientierten Unternehmen, in dem ich meine Kenntnisse in DATEV und Excel einbringen und weiterentwickeln kann.',
    'work_experience': [
        {
            'position': 'Finanzbuchhalter',
            'period': '02/2021 -- heute',
            'company': 'Dienstleistungsunternehmen (KMU), Berlin',
            'tasks': [
                'Bearbeitung von Eingangs- und Ausgangsrechnungen',
                'Abstimmung von Konten und Unterstützung bei Monatsabschlüssen',
                'Erstellung von Umsatzsteuer-Voranmeldungen',
                'Nutzung von DATEV Unternehmen online und digitalen Buchhaltungslösungen',
                'Zusammenarbeit mit Steuerberatern und internen Abteilungen'
            ]
        },
        {
            'position': 'Kaufmännischer Sachbearbeiter',
            'period': '09/2019 -- 01/2021',
            'company': 'Handelsunternehmen, Berlin',
            'tasks': [
                'Rechnungsprüfung und Bearbeitung des Zahlungsverkehrs',
                'Unterstützung in der vorbereitenden Buchhaltung',
                'Erstellung von Auswertungen in MS Excel (Pivot-Tabellen, einfache Kalkulationen)'
            ]
        }
    ],
    'education': [
        {
            'degree': 'Weiterbildung zum Finanzbuchhalter (IHK)',
            'period': '2021 -- 2022',
            'institution': 'IHK Berlin'
        },
        {
            'degree': 'Ausbildung zum Industriekaufmann',
            'period': '2016 -- 2019',
            'institution': 'Industriebetrieb, Berlin'
        }
    ],
    'skills': {
        'fachkompetenz': [
            'Laufende Finanzbuchhaltung (Debitoren, Kreditoren, Bank)',
            'Umsatzsteuer-Voranmeldungen',
            'Unterstützung bei Monatsabschlüssen'
        ],
        'software': [
            'DATEV Unternehmen online',
            'MS Excel (Pivot-Tabellen, Grundkenntnisse Power Query)'
        ],
        'languages': [
            'Deutsch: Muttersprache',
            'Englisch: Grundkenntnisse'
        ],
        'personal_strengths': [
            'Digitalaffin und offen für Prozessoptimierung',
            'Strukturiert, zuverlässig und teamorientiert',
            'Schnelle Auffassungsgabe und Lernbereitschaft'
        ]
    }
}

# LaTeX-Template laden
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# LaTeX-Datei erstellen
output_tex = 'generated_cv.tex'
with open(output_tex, 'w', encoding='utf-8') as f:
    f.write(template.render(cv=cv_data))  # Hier wird cv_data korrekt übergeben

# PDF kompilieren
subprocess.run(['pdflatex', output_tex])

print("✅ PDF erfolgreich erstellt.")
