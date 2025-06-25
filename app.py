import streamlit as st
import subprocess
from jinja2 import Environment, FileSystemLoader
import os
import uuid

# Streamlit App Titel
st.title("Lebenslauf Generator")

# Eingabeformular
st.header("Lebenslauf-Daten eingeben")

# Basisdaten
job_title = st.text_input("Berufsbezeichnung", "Finanzbuchhalter")
name = st.text_input("Name", "[Anonymisiert]")
birth_year = st.text_input("Geburtsjahr", "1996")
location = st.text_input("Wohnort", "Berlin")
family_status = st.text_input("Familienstand", "Ledig")
nationality = st.text_input("Staatsangehörigkeit", "Deutsch")

# Berufsziel
career_goal = st.text_area("Berufsziel", "Digitalaffiner Finanzbuchhalter...")

# Ausbildung
st.header("Ausbildung")
education = []
for i in range(1, 4):
    degree = st.text_input(f"Abschluss {i}", "")
    institution = st.text_input(f"Bildungseinrichtung {i}", "")
    year = st.text_input(f"Abschlussjahr {i}", "")
    if degree and institution and year:
        education.append({"degree": degree, "institution": institution, "year": year})

# Kenntnisse
st.header("Kenntnisse")
professional_skills = st.text_area("Berufliche Kenntnisse (Kommagetrennt)", "Finanzbuchhaltung, Controlling, DATEV")
personal_skills = st.text_area("Persönliche Stärken (Kommagetrennt)", "Teamfähigkeit, Selbstorganisation, Zuverlässigkeit")

# Sprachen
st.header("Sprachkenntnisse")
languages = st.text_area("Sprachen (Beispiel: Deutsch - Muttersprache, Englisch - Fließend)", "Deutsch - Muttersprache, Englisch - Fließend")

# Button zur PDF-Erstellung
if st.button("Lebenslauf generieren"):
    # Temporärer Ordner für Dateien
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Daten für das Template
    cv_data = {
        "job_title": job_title,
        "name": name,
        "birth_year": birth_year,
        "location": location,
        "family_status": family_status,
        "nationality": nationality,
        "career_goal": career_goal,
        "education": education,
        "skills": {
            "professional": [skill.strip() for skill in professional_skills.split(",") if skill.strip()],
            "personal": [skill.strip() for skill in personal_skills.split(",") if skill.strip()]
        },
        "languages": [lang.strip() for lang in languages.split(",") if lang.strip()]
    }

    # Template laden
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('cv_template.tex')

    # Einzigartige Dateinamen
    file_id = str(uuid.uuid4())
    tex_file = os.path.join(output_dir, f"{file_id}.tex")
    pdf_file = os.path.join(output_dir, f"{file_id}.pdf")

    # LaTeX-Datei schreiben
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(template.render(cv=cv_data))

    # LaTeX zu PDF kompilieren
    subprocess.run(['pdflatex', '-output-directory', output_dir, tex_file])

    # PDF zum Download bereitstellen
    with open(pdf_file, "rb") as f:
        st.success("PDF erfolgreich erstellt!")
        st.download_button("PDF herunterladen", f, file_name="Lebenslauf.pdf")
