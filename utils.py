import os
import requests
from bs4 import BeautifulSoup

def clean_description(content) -> str:
  if not content:
    return ""

  soup = BeautifulSoup(content, "html.parser")
  return soup.get_text(separator=" ", strip=True)


def send_message(msg: str):
  if not msg:
    return
  
  requests.post(
    url=os.getenv("DISCORD_WEBHOOK_URL"),
    headers={
      "Content-Type": "application/json"
    },
    json={
      "content": msg.strip()
    }
  )
