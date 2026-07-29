import time
import locale
from datetime import datetime, timezone
from summary import generate_summary
from feed import read_feed_rss
from utils import send_message

# On configure la langue en français pour la date
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

# Date actuelle
now = datetime.now(timezone.utc)
date_str = now.strftime("%d %B %Y")

# Limite de caractères par message
max_length = 1900


def main():
  try:
    all_articles = read_feed_rss()
    summary = generate_summary(all_articles)

    if len(summary) <= max_length:
      send_message(summary)
      return

    # On fait un découpage par ligne
    lines = summary.split("\n")
    current_chunk = ""

    for line in lines:
      if len(current_chunk) + len(line) + 1 > max_length:
        send_message(current_chunk)
        time.sleep(1)

        current_chunk = line + "\n"
      else:
        current_chunk += line + "\n"

    # On envoie le dernier morceau restant s'il existe
    if current_chunk.strip():
      send_message(current_chunk)

  except Exception as e:
    print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
  main()
