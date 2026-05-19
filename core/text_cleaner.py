import re
import nltk

from nltk.tokenize import word_tokenize


required_packages = [

    "punkt",

    "punkt_tab"
]


for package in required_packages:

    try:

        nltk.data.find(f"tokenizers/{package}")

    except LookupError:

        nltk.download(package)


class TextCleaner:

    @staticmethod
    def normalize_text(text):

        text = text.lower()

        text = re.sub(
            r"http\\S+",
            "",
            text
        )

        text = re.sub(
            r"[^a-zA-Z\\s]",
            "",
            text
        )

        text = re.sub(
            r"\\s+",
            " ",
            text
        )

        return text.strip()

    @staticmethod
    def tokenize_text(text):

        clean_text = (
            TextCleaner
            .normalize_text(text)
        )

        return word_tokenize(clean_text)