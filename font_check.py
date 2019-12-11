from fontTools.ttLib import TTCollection, TTFont

def load_font(font_path):
    """
    Read ttc, ttf, otf font file, return a TTFont object
    """

    # ttc is collection of ttf
    if font_path.endswith('ttc'):
        ttc = TTCollection(font_path)
        # assume all ttfs in ttc file have same supported chars
        return ttc.fonts[0]

    if font_path.endswith('ttf') or font_path.endswith('TTF') or font_path.endswith('otf'):
        ttf = TTFont(font_path, 0, allowVID=0,
                     ignoreDecompileErrors=True,
                     fontNumber=-1)

        return ttf

use = []
import glob
from tqdm import tqdm
for font_path in tqdm(glob.glob('data/fonts/vie/*')):
    try:
        tff = load_font(font_path)
        if tff is None:
            continue
    except:
        continue
    print(font_path)
    use.append(font_path)

with open('./data/fonts_list/vie.txt', 'w') as f:
    for item in use:
        f.write("%s\n" % item)
