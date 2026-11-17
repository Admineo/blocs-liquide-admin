# Plateforme d'administration à distance de BLOCS

`admin.html` est une page à part (à ouvrir dans Safari/Chrome, sur téléphone ou ordinateur). Elle modifie un fichier `config.json` que le jeu télécharge à chaque lancement. Résultat : vous changez la difficulté, les pièces, les rotations ou publiez une annonce **sans renvoyer l'app aux stores**.

## Ce qu'on peut modifier à distance
- Nombre de rotations par partie (0 à 20) et fréquence des blocs spéciaux (5 à 60)
- Pour chaque niveau : objectif, annulations, cases pré-remplies, rampe de difficulté, % d'ondes
- Niveaux sans fin : pas d'objectif, annulations, pré-remplissage maximum
- Retirer des pièces du tirage (29 d'origine) et en ajouter (12 max, dessinées sur 5 × 5)
- Une annonce unique FR/EN affichée une fois à chaque joueur
- Historique des 10 dernières publications, retour en arrière en un clic

Ce sont uniquement des **données** (nombres, formes, texte). Aucun code n'est téléchargé : c'est compatible avec la règle Apple 2.5.2. Le jeu valide et borne tout ; un fichier invalide est ignoré. Sans réseau, le jeu garde le dernier réglage reçu.

## Mise en place (une seule fois, ~10 minutes)
1. Créez un compte sur github.com puis un dépôt **public** nommé par ex. `blocs-config`.
2. Dans le dépôt : Settings → Pages → Source « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. Envoyez dans le dépôt le fichier `config.default.json` renommé en `config.json` (Add file → Upload files).
4. Créez la clé : GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate. Repository access : *Only select repositories* → `blocs-config`. Permissions : **Contents : Read and write**. Durée : 1 an. Copiez-la (`github_pat_…`).
5. Adresse publique du fichier : `https://VOTRENOM.github.io/blocs-config/config.json`. Vérifiez qu'elle s'affiche dans un navigateur (patientez quelques minutes la première fois).
6. Ouvrez cette adresse dans `remote/rc_url.txt` (une seule ligne, en https), puis relancez `python3 build.py` : le jeu saura où lire. **À faire avant de fabriquer les apps des stores.**
7. Hébergez `admin.html` où vous voulez (par ex. dans le même dépôt, dossier `admin/`, ou gardez-le sur votre téléphone). Ne le laissez pas indexer ; la page n'a de pouvoir qu'avec votre clé.

## Utilisation
1. Ouvrez `admin.html`, saisissez compte, dépôt et clé, puis « Se connecter et charger ».
2. Modifiez. « Tester dans le jeu » ouvre la version web du jeu avec vos réglages, sans rien publier (renseignez l'adresse du jeu web ; fonctionne sur la version web, pas dans l'app installée).
3. « Publier » : GitHub Pages diffuse en 1 à 10 minutes ; la page vérifie ensuite que la révision est en ligne. Les joueurs la reçoivent à leur prochain lancement.
4. Une erreur ? Section Historique → « Charger » une ancienne version → Publier.

## Sécurité
- La clé n'a accès qu'à ce dépôt. Ne cochez « Mémoriser la clé » que sur votre appareil personnel. Si elle fuit, révoquez-la sur GitHub.
- Le fichier est public : n'y mettez rien de confidentiel.
- Sans connexion : « Travailler sans connexion », puis « Télécharger config.json » et envoyez-le à la main dans le dépôt.

## Limites
- Les changements s'appliquent aux parties lancées après réception.
- La connexion GitHub réelle n'a pu être testée qu'avec un faux serveur : faites un premier essai simple (ex. rotations 5 → 6) pour valider votre installation.
