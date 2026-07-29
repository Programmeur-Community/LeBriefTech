import feedparser
from utils import clean_description


def read_feed_rss() -> list:
  feed = feedparser.parse("https://dev.to/feed/")

  articles_to_send = []

  entries = feed["entries"]
  for entry in entries:
    title = entry["title"]
    clean_desc = clean_description(entry["description"])
    articles_to_send.append(f"Titre : {title}\nContenu : {clean_desc}")

  return articles_to_send
