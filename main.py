from fnmatch import translate
import json
from typing import Type
from urllib.parse import ParseResultBytes

from click import File
from exceptions import NoTranslationConfigError, ConfigInputError, ConfigOutputError, NewTranslationDictError, NewConfigDictError
from fpdf import FPDF
from os.path import exists

class Color:
    def __init__(self, R: int, G: int, B: int) -> None:
        try:
            assert type(R) is int
            self.R = R
            assert type(G) is int
            self.G = G
            assert type(B) is int
            self.B = B
        except AssertionError:
            raise AssertionError("All initialization values must be of the correct type.")

class Translation:
    def __init__(self, xPos: int, yPos: int, textColor: Color,\
         backgroundColor: Color, originalText: str, translatedText: str) -> None:
        try:
            assert type(xPos) is int
            self.xPos = xPos
            assert type(yPos) is int
            self.yPos = yPos
            assert type(textColor) is Color
            self.textColor = textColor
            assert type(backgroundColor) is Color
            self.backgroundColor = backgroundColor
            assert type(originalText) is str
            self.originalText = originalText
            assert type(translatedText) is str
            self.translatedText = translatedText
        except AssertionError:
            raise AssertionError("All initialization values must be of the correct type.")

class TranslationConfig:
    def __init__(self, originalFileName: str, outputFileName: str) -> None:
        try:
            assert type(originalFileName) is str
            self.originalFileName = originalFileName
            assert type(outputFileName) is str
            self.outputFileName = outputFileName
            self.translations = []
        except AssertionError:
            raise AssertionError("All initialization values must be of the correct type.")
    
    def add_translation(self, translation: Translation) -> None:
        try:
            assert type(translation) is Translation
            self.translations.append(translation)
        except AssertionError:
            raise AssertionError("Provided object is not a Translation.")


def import_tr_as_dict(filepath: str) -> dict:
    if not exists(filepath):
        raise NoTranslationConfigError
    try:
        with open(filepath, 'r') as f:
            out_dict: dict = json.load(f)
        return out_dict
    except Exception:
        raise ConfigInputError


def output_dict_to_tr(filepath: str, translation_dict: dict) -> None:
    if not exists(filepath):
        f = open(filepath, 'w+')
        f.close()
    try:
        with open(filepath, 'w') as f:
            json.dump(translation_dict, f, indent=4)
    except Exception:
        raise ConfigOutputError


def create_new_config_dict(originalFileName: str, outputFileName: str) -> dict:
    try:
        assert type(originalFileName) is str
        assert type(outputFileName) is str
        
        if 0 in [len(originalFileName), len(outputFileName)] or '.' not in originalFileName or \
            '.' not in outputFileName or outputFileName.split('.')[1].lower() != 'tr':
            raise FileNotFoundError

        return { 'originalFileName': originalFileName, 'outputFileName': outputFileName, 'translations': [] }
    except AssertionError:
        raise AssertionError("Input variables should be of the appropriate type.")
    except FileNotFoundError:
        raise FileNotFoundError("Original and output files must have the appropriate naming convention!")
    except Exception:
        raise NewConfigDictError


def create_new_translation_dict() -> dict:
    try:
        return {}
    except AssertionError:
        raise AssertionError("Input variables should be of the appropriate type.")
    except Exception:
        raise NewTranslationDictError


def main() -> None:
    create_new_config_dict

if __name__ == '__main__':
    main()