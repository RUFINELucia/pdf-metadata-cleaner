#!/usr/bin/env python3
"""
clean_metadata.py

Petit utilitaire pour supprimer ou remplacer les métadonnées d'un PDF.
Utilise PyPDF2.

Exemples :
    python clean_metadata.py --input examples/sample.pdf
    python clean_metadata.py --input examples/ --output cleaned/
    python clean_metadata.py --input file.pdf --set-title "Anonyme" --set-author "N/A"
"""

import argparse
import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


def clean_pdf_metadata(input_pdf: Path, output_pdf: Path, custom_meta: dict, dry_run: bool = False):
    """
    Nettoie un fichier PDF en supprimant/remplaçant ses métadonnées.
    """
    try:
        reader = PdfReader(str(input_pdf))
        writer = PdfWriter()

        # Copier toutes les pages
        for page in reader.pages:
            writer.add_page(page)

        # Appliquer métadonnées (vides ou custom)
        if custom_meta:
            writer.add_metadata(custom_meta)
        else:
            writer.add_metadata({})  # vide

        if dry_run:
            print(f"[DRY-RUN] {input_pdf} -> {output_pdf}")
            return

        # Écriture du fichier nettoyé
        with open(output_pdf, "wb") as f_out:
            writer.write(f_out)
        print(f"[OK] {input_pdf} -> {output_pdf}")

    except Exception as e:
        print(f"[ERREUR] Impossible de traiter {input_pdf}: {e}")


def process_path(input_path: Path, output_dir: Path, custom_meta: dict, dry_run: bool):
    """
    Traite un fichier ou un dossier contenant des PDFs.
    """
    if input_path.is_file() and input_path.suffix.lower() == ".pdf":
        output_file = output_dir / input_path.name
        clean_pdf_metadata(input_path, output_file, custom_meta, dry_run)
    elif input_path.is_dir():
        for pdf_file in input_path.glob("*.pdf"):
            output_file = output_dir / pdf_file.name
            clean_pdf_metadata(pdf_file, output_file, custom_meta, dry_run)
    else:
        print(f"[SKIP] {input_path} n'est pas un fichier PDF valide.")


def main():
    parser = argparse.ArgumentParser(description="Supprime les métadonnées d'un fichier PDF.")
    parser.add_argument("--input", "-i", type=Path, required=True, help="Fichier ou dossier PDF à nettoyer")
    parser.add_argument("--output", "-o", type=Path, default=Path("cleaned/"), help="Dossier de sortie (par défaut: cleaned/)")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Mode simulation (aucun fichier écrit)")
    parser.add_argument("--set-title", help="Définir un titre personnalisé")
    parser.add_argument("--set-author", help="Définir un auteur personnalisé")
    parser.add_argument("--set-subject", help="Définir un sujet personnalisé")
    parser.add_argument("--set-keywords", help="Définir des mots-clés personnalisés (séparés par des virgules)")
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)

    custom_meta = {}
    if args.set_title:
        custom_meta["/Title"] = args.set_title
    if args.set_author:
        custom_meta["/Author"] = args.set_author
    if args.set_subject:
        custom_meta["/Subject"] = args.set_subject
    if args.set_keywords:
        custom_meta["/Keywords"] = args.set_keyword

