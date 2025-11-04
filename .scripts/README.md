# Karuta Scripts

Ces scripts sont là pour assister à la gestion du deck.

Attention : Si le deck n'est pas dans le dossier parent aux scripts, utiliser le paramètre `--deck-path DECK_PATH`

### download-audio.py

Dépendances : `pip install pydub yt-dlp requests` et ffmpeg (sur windows `winget install ffmpeg`, sur debian-like `apt install ffmpeg`)

Utilisation : `python download-audio.py [--force]`

### gen-readme.py

Dépendances : Aucune

Utilisation : `python gen-readme.py`

### gen-cards-pdf.py

Dépendances : `pip install fpdf2`  

Utilisation : `python gen-cards-pdf.py [destination folder]`  

### new-to-old-convert.py

Dépendances : `pip install pillow numpy`

Utilisation : `python new-to-old-convert.py [old deck format folder]`