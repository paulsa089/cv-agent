import streamlit as st
from jinja2 import Environment, FileSystemLoader

# Initialisierung des Session States
if 'cv_generated' not in st.session_state:
    st.session_state['cv_generated'] = False

# Titel
st.title("Lebenslauf Generator")

# Eingabeformular
st.header("Lebenslauf-Daten eingeben")

# Formularfelder
job_title = st.text_input("Berufsbezeichnung", "Finanzbuchhalter")
name = st.text_input("Name", "[Anonymisiert]")
birth_year = st.text_input("Geburtsjahr", "1996")
location = st.text_input("Wohnort", "Berlin")
family_status = st.text_input("Familienstand", "Ledig")
nationality = st.text_input("Staatsangehörigkeit", "Deutsch")
career_goal = st.text_area("Berufsziel", "Digitalaffiner Finanzbuchhalter...")

# Ausbildung
st.subheader("Ausbildung")
education_entries = st.text_area(
    "Gib die Ausbildung ein (eine pro Zeile, z.B. '2015-2018: Ausbildung zum Steuerfachangestellten')"
)
education = [entry.strip() for entry in education_entries.split("\n") if entry.strip()]

# Kenntnisse
st.subheader("Kenntnisse")
professional_skills = st.text_input("Fachliche Kenntnisse (z.B. SAP, DATEV, MS Excel)", "")
personal_skills = st.text_input("Persönliche Kompetenzen (z.B. Teamfähigkeit, Flexibilität)", "")

# Sprachen
st.subheader("Sprachen")
language_entries = st.text_area(
    "Gib die Sprachen ein (eine pro Zeile, z.B. 'Englisch: Verhandlungssicher')"
)
languages = [entry.strip() for entry in language_entries.split("\n") if entry.strip()]

# Daten zusammenfassen
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
        "professional": professional_skills,
        "personal": personal_skills
    },
    "languages": languages
}

# Button zur "Generierung"
if st.button("Lebenslauf generieren"):
    st.session_state['cv_generated'] = True
    st.session_state['cv_data'] = cv_data

# Ausgabe nach Klick
if st.session_state['cv_generated']:
    st.success("Lebenslauf-Daten erfolgreich erfasst!")
    st.write("Hier sind die eingegebenen Daten:")
    st.json(st.session_state['cv_data'])

    st.info("Hinweis: PDF-Generierung in Streamlit Cloud nicht möglich – lokale Ausführung notwendig für PDF.")

