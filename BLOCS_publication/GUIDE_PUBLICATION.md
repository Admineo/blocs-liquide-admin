# Guide de publication de BLOCS (App Store + Google Play)

Ce dossier contient tout ce qui se prépare sans Mac ni Android Studio. Les deux dernières étapes (fabriquer le fichier final et l'envoyer) se font sur votre ordinateur, avec les outils gratuits d'Apple et de Google : je n'ai pas pu les faire à votre place.

## 0. Ce que contient le dossier

| Élément | Rôle |
|---|---|
| `www/index.html` | **Le jeu pour les stores** (français + anglais, sans menu caché, sans photo de femme) |
| `blocs-perso.html` | **Votre version personnelle** (menu caché code 1140 + photo). **Ne jamais l'envoyer aux stores.** |
| `source/` + `build.py` | Le code source et le script qui fabrique les deux versions (`python3 build.py`) |
| `capacitor/` | Le projet qui transforme le jeu en vraie application Android et iPhone |
| `capacitor/assets/` | Icône, icône Android adaptative, écrans de lancement |
| `store/ios/`, `store/android/` | Captures d'écran FR/EN, icônes 1024 et 512, visuels de présentation Google |
| `store/listing/` | Textes des fiches FR/EN et réponses aux questionnaires |
| `privacy/index.html` | Politique de confidentialité FR + EN, à mettre en ligne |

## 1. Avant de payer quoi que ce soit

1. **Vérifiez le nom.** Cherchez « BLOCS » et « BLOCS - Puzzle Liquide » dans l'App Store et Google Play, et sur la base de marques de l'INPI (data.inpi.fr). Si le nom est pris, changez-le dans `store/listing/*.md` et `capacitor/capacitor.config.json` (`appName`).
2. **Choisissez votre identifiant d'app** (« bundle ID »). Je l'ai mis à `com.bayram.blocs` ; il ne pourra plus changer après publication. Modifiez-le dans `capacitor/capacitor.config.json` si vous voulez autre chose (par exemple `fr.votrenom.blocs`).
3. **Votre e-mail de contact.** Ouvrez `privacy/index.html` et remplacez `VOTRE-ADRESSE@EXEMPLE.COM` (2 endroits, FR et EN).
4. **Mettez la politique de confidentialité en ligne.** Les deux stores exigent une adresse web. Le plus simple et gratuit : créez un compte sur github.com, un dépôt public, envoyez `privacy/index.html`, puis activez « Settings > Pages ». L'adresse ressemblera à `https://votrenom.github.io/blocs/`. Netlify Drop (app.netlify.com/drop) marche aussi : glissez le dossier `privacy`.

## 2. Les comptes développeur

| | Google Play | Apple |
|---|---|---|
| Prix | 25 $ une seule fois | 99 $ par an |
| Où | play.google.com/console | developer.apple.com/programs |
| Délai | vérification d'identité : quelques jours | validation : 1 à 2 jours en général |
| À savoir | **Compte personnel : test fermé obligatoire avec au moins 12 testeurs pendant 14 jours d'affilée** avant la publication (vérifiez la règle actuelle dans la console) | **Un Mac avec Xcode 26 ou plus récent est obligatoire** pour fabriquer l'app iPhone |

Le nom du développeur affiché publiquement sera celui de votre compte (par exemple « Melis et EmrE Bayram » si vous le saisissez ainsi à l'inscription). Conseil : commencez par **Google Play** (pas besoin de Mac) et lancez tout de suite les 14 jours de test, c'est ce qui prend le plus de temps.

## 3. Fabriquer les applications

### 3.1 Installer les outils (une seule fois)
- Node.js (nodejs.org, version LTS)
- Android Studio (developer.android.com/studio)
- Sur Mac seulement : Xcode (App Store Mac) et CocoaPods (`sudo gem install cocoapods` ou `brew install cocoapods`)

### 3.2 Créer les projets
Dans un terminal, depuis le dossier `capacitor` :

```
npm install @capacitor/core
npm install -D @capacitor/cli @capacitor/assets @capacitor/android @capacitor/ios
npm run copy
npx cap add android
npx cap add ios          # Mac uniquement
npm run assets           # fabrique toutes les icônes et écrans de lancement
npm run sync
```

Ensuite, suivez `capacitor/android-notes.txt` (version, orientation portrait, niveau d'API 36) et, pour l'iPhone, `capacitor/ios-Info-plist.txt` (textes d'autorisation photo, iPhone seulement).

### 3.3 Android : le fichier à envoyer
`npm run android` ouvre Android Studio. Puis : *Build > Generate Signed App Bundle / APK > Android App Bundle*. Créez une clé (keystore) **et sauvegardez-la** (deux copies + le mot de passe) : sans elle, impossible de mettre à jour le jeu. Le résultat est un fichier `app-release.aab`.

### 3.4 iPhone : le fichier à envoyer
`npm run ios` ouvre Xcode. Dans la cible « App » : choisissez votre équipe (Team) pour la signature, version `1.0.0`, build `1`, iPhone uniquement. Puis *Product > Archive > Distribute App > App Store Connect > Upload*.
**Sans Mac :** louer un Mac en ligne à l'heure (par exemple MacinCloud), emprunter celui d'un proche, ou utiliser un service de compilation dans le cloud (Codemagic, par exemple). Il faut quand même le compte Apple payant.

## 4. Google Play Console, pas à pas
1. Créer l'application : nom, langue par défaut français, « Jeu », « Gratuit ».
2. *Contenu de l'application* : politique de confidentialité (URL), accès à l'app (tout accessible), publicités (non), classification du contenu, public cible, sécurité des données. Toutes les réponses sont dans `store/listing/infos_communes.md`.
3. *Fiche Play Store* : titre, descriptions (`fiche_fr.md`), icône 512, illustration `feature-graphic_fr.png`, captures `android_fr_*.jpg`. Ajoutez l'anglais comme traduction (`fiche_en.md`).
4. *Tests > Test fermé* : envoyez le `.aab`, ajoutez au moins 12 adresses Gmail de testeurs (famille, amis), envoyez-leur le lien d'inscription. Ils doivent rester inscrits 14 jours d'affilée.
5. Après 14 jours : *Production > Demander l'accès*, répondez au questionnaire, puis envoyez la version en production. Première validation : quelques jours.

## 5. App Store Connect, pas à pas
1. Créer l'identifiant (*Certificates, Identifiers > Identifiers*) avec le bundle ID choisi.
2. *Mes apps > + > Nouvelle app* : nom, langue principale français, bundle ID, SKU (n'importe quel code, par ex. `blocs001`).
3. Envoyer la build depuis Xcode (étape 3.4). Elle apparaît après quelques minutes.
4. Remplir la fiche : sous-titre, texte promotionnel, description, mots-clés (`fiche_fr.md`), captures 6,9" (`ios_fr_*.jpg`), icône (incluse dans la build), URL de confidentialité, catégorie Jeux > Puzzle, prix gratuit, droits d'auteur. Ajouter l'anglais comme seconde langue.
5. *Confidentialité de l'app* : « Aucune donnée collectée ». *Classification d'âge* : tout à « Aucun ».
6. Coller les « Notes de révision » (fichier `infos_communes.md`) et envoyer pour validation. Délai habituel : 1 à 2 jours.
7. Conseil : testez d'abord via **TestFlight** sur votre propre iPhone.

## 6. Pourquoi une app peut être refusée (et ce qui est déjà prévu)
- *Fonctions cachées* (règle Apple 2.3.1) : la version stores **n'a pas** de menu caché. N'y remettez jamais `blocs-perso.html`.
- *Droits d'auteur* : la photo de femme a été retirée de la version stores. Si vous ajoutez des images, des sons ou des polices, vous devez en avoir les droits.
- *« App qui n'est qu'un site web »* (règle 4.2) : le jeu fonctionne hors connexion, a de vrais contenus (niveaux sans fin, rotations, bombes, records) et une icône/écran de lancement. Décrivez-le comme un jeu complet, ce qui est le cas.
- *Autorisations photo/appareil photo* : les textes sont prévus dans `ios-Info-plist.txt`.
- *Plantage ou écran blanc* : testez sur un vrai téléphone avant d'envoyer.

## 7. Mises à jour
Modifiez `source/blocs.src.html`, lancez `python3 build.py`, puis `npm run sync` dans `capacitor`. Augmentez `versionCode` (Android) et le numéro de build (iPhone) à chaque envoi.

## 7 bis. Modifier le jeu à distance (plateforme d'administration)
Le dossier `remote/` contient `admin.html` : une page à part pour changer la difficulté, les pièces, les rotations et publier des annonces sans repasser par les stores. Mise en place et mode d'emploi : `remote/README_PLATEFORME.md`.
- **Avant de fabriquer les apps** : mettez l'adresse publique de `config.json` dans `remote/rc_url.txt`, puis `python3 build.py`.
- Apple (règle 2.5.2) : seules des données sont téléchargées, jamais du code ; ne décrivez pas cela comme « changer les fonctions de l'app ». Dans la politique de confidentialité (déjà mise à jour), le fichier public est mentionné.
- Google Play, section « Sécurité des données » : toujours « aucune donnée collectée ».

## 8. Ce qui n'est pas inclus (à savoir)
- Les fichiers finaux `.aab` et `.ipa` : ils se fabriquent sur votre machine (étape 3).
- Aucun test sur de vrais téléphones n'a été fait : seulement des essais dans un navigateur de la taille d'un iPhone et d'un Android.
- Pas de classement en ligne entre amis (il faudrait Game Center / Google Play Jeux ou un serveur). Le partage de score passe par le menu de partage du téléphone.
- Les données (records, partie en cours) sont gardées dans l'espace de stockage de l'app. Dans de rares cas (téléphone presque plein), iOS peut le vider ; un stockage natif pourra être ajouté plus tard.
- Prix, délais et règles des stores changent : vérifiez-les dans les consoles au moment de vous inscrire.
