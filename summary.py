from google import genai
from google.genai import types
from dotenv import load_dotenv

# On charge les variables d'environnement
load_dotenv()

client = genai.Client()


def generate_summary(articles: list) -> str | None:
  full_text_input = "\n\n---\n\n".join(articles)
  system_instruction = """
    Tu es un assistant spécialisé en veille technologique pour des développeurs et créateurs de contenu tech.
    Ta mission est de lire les articles fournis et d'en faire un résumé clair, synthétique et captivant sous forme de liste.

    Règles de formatage :
    - Utilise des puces et démarre chaque point par un emoji pertinent (ex : 🚀, ⚡, 🛡️, 💡).
    - Mets en **gras** les termes clés ou les outils importants.
    - Sois concis : 2 à 3 phrases maximum par actualité majeure.
    - Sélectionne uniquement les 3 à 5 actualités les plus pertinentes ou impactantes.
    - Le résumé doit faire moins de 2000 caractères.
    - Garde un ton professionnel mais dynamique.
  """

  response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[f"Voici les actualités du jour à résumer :\n\n{full_text_input}"],
    config=types.GenerateContentConfig(
      system_instruction=system_instruction,
      temperature=0.3
    )
  )

  return response.text
