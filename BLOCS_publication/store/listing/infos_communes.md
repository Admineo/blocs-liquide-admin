# Informations communes aux deux stores

| Champ | Valeur à saisir |
|---|---|
| Catégorie | Jeux > Puzzle (Apple : Games > Puzzle ; Google : Game > Puzzle) |
| Prix | Gratuit |
| Achats intégrés / publicités | Aucun / Aucune |
| Langues de la fiche | Français (France) + Anglais |
| Copyright (Apple) | © 2026 Melis et EmrE Bayram |
| URL de la politique de confidentialité | l'adresse où vous publierez `privacy/index.html` |
| URL d'assistance (Apple) | la même page, ou une page avec votre e-mail |
| E-mail de contact (Google) | votre adresse e-mail |
| Appareils | iPhone uniquement (décocher iPad) ; Android téléphones |

## Questionnaires
- **Apple – Confidentialité de l'app** : « Aucune donnée collectée » (Data Not Collected).
- **Apple – Classification d'âge** : répondre « Aucun / Jamais » à toutes les questions → 4+.
- **Apple – Chiffrement** : la clé `ITSAppUsesNonExemptEncryption = false` est déjà dans `capacitor/ios-Info-plist.txt`.
- **Google – Sécurité des données** : ne collecte ni ne partage aucune donnée ; pas de chiffrement en transit à déclarer (aucun envoi).
- **Google – Classification du contenu (IARC)** : jeu de réflexion ; violence, sexe, jeux d'argent, langage : « Non » partout → PEGI 3 / Tout public.
- **Google – Public cible** : choisir « 13 ans et plus » (évite les règles supplémentaires « Famille » ; le jeu ne collecte rien de toute façon).
- **Google – Publicités** : « Non, l'application ne contient pas de publicités ».
- **Google – Accès à l'application** : « Toutes les fonctionnalités sont accessibles sans identifiant ».

## Notes pour l'équipe de validation Apple (champ « Notes de révision », en anglais)
BLOCS is a single-player offline puzzle game. No account or login is required and there are no hidden or undocumented features. The “Background: choose a photo” option in the Menu uses the system photo picker; the chosen image is stored only on the device. The app does not collect or transmit any data.

## Captures d'écran à envoyer
- Apple iPhone 6,9" : `store/ios/` → fichiers `ios_fr_*.jpg` (1320 × 2868) pour la fiche FR, `ios_en_*.jpg` pour l'EN.
- Google téléphone : `store/android/` → `android_fr_*.jpg` / `android_en_*.jpg` (1080 × 2160).
- Google « Illustration de présentation » : `feature-graphic_fr.png` / `feature-graphic_en.png` (1024 × 500).
- Icône Google : `icon-512.png` ; icône Apple : `app-icon-1024.png` (fournie aussi à Xcode par `npm run assets`).
