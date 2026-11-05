from PIL import Image
import numpy as np

for name, suffix in [('logo-color', 'color'), ('logo-dark', 'dark')]:
    im = Image.open(f'assets/img/{name}.png')
    arr = np.array(im)
    alpha = arr[:, :, 3]
    
    # 1. Full logo cropped to bounds
    y_idx, x_idx = np.where(alpha > 10)
    full_crop = im.crop((x_idx.min(), y_idx.min(), x_idx.max()+1, y_idx.max()+1))
    full_crop.save(f'assets/img/logo-{suffix}-clean.png')
    print(f'Saved logo-{suffix}-clean.png, size={full_crop.size}')
    
    # 2. Isotipo (MW icon alone without reflection)
    y_iso, x_iso = np.where(alpha[:470] > 20)
    iso_clean = im.crop((x_iso.min(), y_iso.min(), x_iso.max()+1, y_iso.max()+1))
    iso_clean.save(f'assets/img/isotipo-{suffix}.png')
    print(f'Saved isotipo-{suffix}.png, size={iso_clean.size}')
    
    # 3. Logotipo (Wordmark MAKIPURA WORLD alone)
    y_text, x_text = np.where(alpha[570:] > 20)
    text_clean = im.crop((x_text.min(), 570 + y_text.min(), x_text.max()+1, 570 + y_text.max()+1))
    text_clean.save(f'assets/img/logotipo-{suffix}.png')
    print(f'Saved logotipo-{suffix}.png, size={text_clean.size}')

print('All logo assets successfully extracted!')
