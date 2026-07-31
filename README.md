# LeBriefTech

LeBriefTech est un petit projet Python conçu pour automatiser la veille technologique.

## Objectif

L'objectif principal de ce projet est de recevoir chaque matin un message automatique dans un salon Discord via un webhook, afin de consulter rapidement un résumé des dernières actualités tech.

Ce système a été créé pour éviter de passer du temps à parcourir plusieurs blogs, newsletters ou sources d'information dispersées. Il permet de centraliser une lecture synthétique et de partager facilement ces informations avec les membres d'un groupe ou d'une communauté.

## Comment ça fonctionne

Chaque exécution du programme :

1. Récupère des articles depuis un flux RSS technologique (en occurence celui de [DEV.TO](https://dev.to/)),
2. Nettoie leur contenu,
3. Génère un résumé à l'aide de l'API Gemini,
4. Envoie ce résumé dans un salon Discord via un webhook.

Si le résumé est trop long, il peut être envoyé en plusieurs messages pour rester lisible.

## Prérequis

Avant de lancer le projet, il vous faut :

- Python 3.10 ou plus
- Un compte Google AI avec une clé API Gemini
- Un webhook Discord configuré sur le salon souhaité

## Installation

1. Cloner le projet.

```bash
git clone https://github.com/Programmeur-Community/LeBriefTech
```

```bash
cd LeBriefTech
```

2. Créer un environnement virtuel :

```bash
python -m venv venv
```

3. Activer l'environnement virtuel :
   - Sous Windows (PowerShell) :

     ```bash
     ./venv/Scripts/activate
     ```

   - Sous macOS/Linux :

     ```bash
     source .venv/bin/activate
     ```

4. Installer les dépendances :

```bash
pip install -r requirements.txt
```

5. Créer un fichier `.env` à la racine du projet avec les variables suivantes :

```env
GEMINI_API_KEY=votre_cle_api_gemini
DISCORD_WEBHOOK_URL=votre_url_webhook_discord
```

## Lancement

Pour exécuter le programme manuellement :

```bash
python main.py
```

Le script enverra alors le résumé dans votre salon Discord.

## Automatisation

Le projet utilise **GitHub Actions** pour exécuter le script à une heure donnée. Assurez-vous d'avoir créer votre repositorie et pousser le projet.

Le workflow est créé dans dossier `.github/workflows` et envoie automatiquement le résumé chaque matin à l'heure définie par la planification CRON.

## Structure du projet

- `main.py` : point d'entrée du programme
- `feed.py` : récupération des articles depuis le flux RSS
- `summary.py` : génération du résumé via Gemini
- `utils.py` : nettoyage du texte et envoi du message Discord
- `requirements.txt` : dépendances Python

## À noter

Ce projet est volontairement simple et modulaire. Il peut être facilement amélioré pour :

- Ajouter d'autres sources d'actualités
- Changer le format du résumé
- Envoyer les messages à plusieurs canaux
- Automatiser l'envoi à une heure précise chaque jour.

---

## Auteur

- [**Programmeur**](https://programmeur-community.vercel.app/)

  Pour tout contact ou besoin de collaboration, cliquez [ici](https://programmeur-community.vercel.app/contact).

### Rejoinez-nous

- Facebook : [ici](https://web.facebook.com/profile.php?id=61555138603557)
- Discord : [ici](https://discord.gg/UUbh5zQmX)
