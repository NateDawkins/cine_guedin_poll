# 🎬 Ciné Guedin - Bot Discord de sondage hebdomadaire

Un bot Discord simple pour organiser des séances de cinéma en votant sur le jour préféré de la semaine !  
Le bot poste automatiquement un sondage tous les **dimanches à 11h**, ou à la demande via une commande `/cine`.

## 📌 Fonctionnalités

- 📅 Envoi automatique d’un sondage tous les dimanches à 11h.
- 💬 Commande slash `/cine` pour lancer le sondage manuellement.
- 🗳️ Propose les 7 jours de la semaine en réactions (émojis).
- 🧩 Facile à configurer et à déployer.

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-user/cine-guedin-bot.git
cd cine-guedin-bot
```

### 2. Créer et configurer un fichier .env
Crée un fichier .env à la racine du projet et ajoute les variables suivantes :
```bash
DISCORD_TOKEN=ton_token_discord
GUILD_ID=ton_id_de_serveur
CHANNEL_ID=ton_id_du_channel
```

### 3. Installer les dépendances
```bash
pip install discord
pip intall dotenv
```
## 🚀 Utilisation
Lancer le bot en local :
```bash
python bot_cine.py
```
