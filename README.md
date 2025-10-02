# pdf-metadata-cleaner
Petit outil qui supprime les métadonnées d’un fichier PDF, pour protéger l’anonymat en ligne. Utilise PyPDF2.
<p align="center">
  <img src="lucia-rufine-logo.jpg" alt="lucia-rufine" width="400"/>
</p></br>
<a href="https://luciarufine.netlify.app/">Pour plus de détails sur la protection de l'anonymat cliquez ici !</a>
</p>

## Description

`pdf-metadata-cleaner` est un utilitaire en Python permettant de lire un fichier PDF et d'en retirer les métadonnées (title, author, subject, keywords, custom metadata, etc.). L'objectif est de fournir une façon simple et reproductible de nettoyer les métadonnées avant partage.

> ⚠️ Utilise cet outil de façon responsable. Le retrait de métadonnées ne garantit pas l'anonymat complet (d'autres traces peuvent exister dans le contenu ou la structure du PDF).

## Fonctionnalités

- Supprime les métadonnées standards (Title, Author, Subject, Keywords, Creator, Producer, CreationDate, ModDate).
- Option pour remplacer les métadonnées par des valeurs vides ou par des valeurs personnalisées.
- Traitement d'un fichier unique ou d'un dossier contenant plusieurs PDFs.
- Sauvegarde des fichiers nettoyés dans un dossier de sortie (par défaut `cleaned/`).
- Mode `--dry-run` pour simuler les changements sans écrire de fichiers.

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/TON_COMPTE/pdf-metadata-cleaner.git
cd pdf-metadata-cleaner
```

2. (Recommandé) Créer un environnement virtuel et installer les dépendances :

```bash
python -m venv .venv
source .venv/bin/activate       # Linux / macOS
.\\.venv\\Scripts\\activate     # Windows
pip install -r requirements.txt
```
requirements.txt contient actuellement : PyPDF2

## Usage 

Nettoyer un fichier PDF :
bash```
python clean_metadata.py --input examples/sample.pdf
```

Nettoyer tous les PDF d'un dossier :
bash```
python clean_metadata.py --input examples/ --output cleaned/
```

Exécution en mode simulation (dry-run) :
bash```
python clean_metadata.py --input examples/sample.pdf --dry-run
```

Remplacer les métadonnées par des valeurs personnalisées :
bash```
python clean_metadata.py --input examples/sample.pdf --set-title "Anonyme" --set-author "N/A"
```

## Structure du dépôt

clean_metadata.py — script principal.

examples/ — exemples de fichiers PDF (fichiers factices ou exemples d'usage).

requirements.txt — dépendances Python.

LICENSE — licence (MIT).

 ## Avertissements & limites

- Le script retire/écrase les métadonnées stockées dans l'en-tête PDF mais ne garantit pas l'absence totale d'informations identifiantes (ex : textes, images, empreintes d'annotations, propriétés d'objets non standards).
- Pour des besoins de confidentialité forts, combiner plusieurs méthodes (reconstruction du PDF, conversion en image puis OCR, inspection manuelle).

## Licence

MIT
