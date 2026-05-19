import spacy
import subprocess
import sys

try:

    nlp = spacy.load("en_core_web_sm")

except:

    subprocess.check_call([
        sys.executable,
        "-m",
        "spacy",
        "download",
        "en_core_web_sm"
    ])

    nlp = spacy.load("en_core_web_sm")


class EntityEngine:

    def extract_entities(self, text):

        try:

            doc = nlp(text)

            entities = []

            for ent in doc.ents:

                if ent.text not in entities:

                    entities.append(ent.text)

            return entities[:6]

        except Exception as e:

            print("Entity Error:", e)

            return []