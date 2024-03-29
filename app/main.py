import annotate_pdf
import extract_image_data
import translate_text
import output_translations
from funcs_classes import TranslationConfig
from os import chdir
from pathlib import Path

chdir(Path(__file__).parent.parent.absolute())

if __name__ == '__main__':
    tr_cfg: TranslationConfig = annotate_pdf.run()
    extract_image_data.run(tr_cfg)
    translate_text.run(tr_cfg)
    output_translations.run(tr_cfg)
