from PIL import Image
import numpy as np
import os, json, re, shutil, argparse
from pathlib import Path

def valid_directory(path):
    if os.path.isdir(path): return path
    else: raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory.")
parser = argparse.ArgumentParser(description="Download and normalize the audio files for the deck")
parser.add_argument("--deck-path", type=valid_directory, help="Path to the deck directory", default=os.path.join(os.path.dirname(__file__), os.path.pardir))
parser.add_argument("--output-path", type=Path, help="Path to the output directory", default=os.path.join(os.path.dirname(__file__), os.path.pardir, 'build'))
args = parser.parse_args()

path = args.deck_path
if not os.path.isabs(path): path = os.path.join(os.curdir, path)
outpath = args.output_path
if not os.path.isabs(outpath): outpath = os.path.join(os.curdir, outpath)

with open(os.path.join(path, 'deck.json'), "r") as file:
    meta = json.load(file)

images = [
    (
        m,
        np.array(Image.open(os.path.join(path, 'Visuals', m["image"])))
    ) for m in meta["cards"]
]

images_cut = [
    (
        m,
        re.sub(r"[\/\\\:\*\?\"\<\>\|]",""," ".join([meta['prefix'], m["anime"], m["numbering"], m["title"]])),
        Image.fromarray(im[35:1075,33:783])
    ) for (m,im) in images
]

for d in 'Sounds','Visuals':
    os.makedirs(os.path.join(outpath, d), exist_ok=True)
with open(os.path.join(outpath, meta["name"]+'.txt'), 'w') as file:
    for (m, n, im) in images_cut:
        print(n)
        file.write(n+"\n")
        im.save(os.path.join(outpath, 'Visuals', n+'.png'))
        shutil.copy(os.path.join(path, 'Sounds', m["audio"]), os.path.join(outpath, 'Sounds', n+'.mp3'))