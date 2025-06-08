# Utilise une image Python légère
FROM python:3.11-slim

# Définit le répertoire de travail
WORKDIR /app

# Empêche Python de générer des fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Active le mode non interactif (utile pour les installations)
ENV DEBIAN_FRONTEND=noninteractive

# Copie les fichiers nécessaires
COPY requirements.txt .
COPY bot_cine.py .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande par défaut
CMD ["python", "bot_cine.py"]