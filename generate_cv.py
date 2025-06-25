import pdfcrowd
from jinja2 import Environment, FileSystemLoader

# Beispiel-Daten - ersetze das mit deinen echten Daten
cv_data = {
    "job_title": "Finanzbuchhalter",
    "name": "Luc Manns",
    "email": "luc.manns@avl-recruiting.de",
    "phone": "+49 151 46330868",
    "birth_year": "1996",
    "location": "Berlin (flexibel innerhalb des Stadtgebiets und Umland)",
    "family_status": "Ledig",
    "nationality": "Deutsch",
    "career_goal": "Digitalaffiner Finanzbuchhalter mit drei Jahren Erfahrung in der operativen Buchhaltung, insbesondere in der Rechnungsbearbeitung und Monatsabschlusserstellung. Ich suche im Raum Berlin eine Position in einem modernen, prozessorientierten Unternehmen, in dem ich meine Kenntnisse in DATEV und Excel einbringen und weiterentwickeln kann.",
    "salary": "48.000 € brutto/Jahr",
    "availability": "Kurzfristig, mit 1 Monat Kündigungsfrist",
    "work_experience": [
        {
            "position": "Finanzbuchhalter",
            "period": "02/2021 -- heute",
            "company": "Dienstleistungsunternehmen (KMU), Berlin",
            "tasks": [
                "Bearbeitung von Eingangs- und Ausgangsrechnungen",
                "Abstimmung von Konten und Unterstützung bei Monatsabschlüssen",
                "Erstellung von Umsatzsteuer-Voranmeldungen",
                "Nutzung von DATEV Unternehmen online und digitalen Buchhaltungslösungen",
                "Zusammenarbeit mit Steuerberatern und internen Abteilungen"
            ]
        },
        {
            "position": "Kaufmännischer Sachbearbeiter",
            "period": "09/2019 -- 01/2021",
            "company": "Handelsunternehmen, Berlin",
            "tasks": [
                "Rechnungsprüfung und Bearbeitung des Zahlungsverkehrs",
                "Unterstützung in der vorbereitenden Buchhaltung",
                "Erstellung von Auswertungen in MS Excel (Pivot-Tabellen, einfache Kalkulationen)"
            ]
        }
    ],
    "education": [
        {
            "degree": "Weiterbildung zum Finanzbuchhalter (IHK)",
            "period": "2021 -- 2022",
            "institution": "IHK Berlin"
        },
        {
            "degree": "Ausbildung zum Industriekaufmann",
            "period": "2016 -- 2019",
            "institution": "Industriebetrieb, Berlin"
        }
    ],
    "skills": {
        "fachkompetenz": [
            "Laufende Finanzbuchhaltung (Debitoren, Kreditoren, Bank)",
            "Umsatzsteuer-Voranmeldungen",
            "Unterstützung bei Monatsabschlüssen"
        ],
        "software": [
            "DATEV Unternehmen online",
            "MS Excel (Pivot-Tabellen, Grundkenntnisse Power Query)"
        ],
        "languages": [
            "Deutsch: Muttersprache",
            "Englisch: Grundkenntnisse"
        ],
        "personal_strengths": [
            "Digitalaffin und offen für Prozessoptimierung",
            "Strukturiert, zuverlässig und teamorientiert",
            "Schnelle Auffassungsgabe und Lernbereitschaft"
        ]
    }
}

# PDFCrowd Zugangsdaten
PDFCROWD_USERNAME = 'paulsa'  # deinen pdfcrowd Username hier eintragen
PDFCROWD_API_KEY = 'e0bd4b588648bfc431efcd2c0df245a2'  # deinen pdfcrowd API Key hier eintragen

def render_template(data):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('cv_template.html')  # Datei mit dem HTML Template (aus vorheriger Antwort)
    return template.render(cv=data)

def generate_pdf(html_content, output_file):
    try:
        client = pdfcrowd.HtmlToPdfClient(PDFCROWD_USERNAME, PDFCROWD_API_KEY)
        pdf = client.convertString(html_content)
        with open(output_file, 'wb') as f:
            f.write(pdf)
        print(f"PDF erfolgreich gespeichert: {output_file}")
    except pdfcrowd.Error as e:
        print(f"PDF-Erstellung fehlgeschlagen: {e}")

if __name__ == "__main__":
    html = render_template(cv_data)
    generate_pdf(html, "lebenslauf.pdf")
