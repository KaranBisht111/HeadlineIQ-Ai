from sklearn.feature_extraction.text import TfidfVectorizer


class KeywordEngine:

    def extract_keywords(
        self,
        text,
        limit=8
    ):

        try:

            vectorizer = TfidfVectorizer(
                stop_words="english",
                max_features=limit
            )

            matrix = vectorizer.fit_transform([text])

            features = vectorizer.get_feature_names_out()

            scores = matrix.toarray()[0]

            ranked = []

            for i in range(len(features)):

                ranked.append(
                    (features[i], scores[i])
                )

            ranked.sort(
                key=lambda x: x[1],
                reverse=True
            )

            return [item[0] for item in ranked]

        except Exception as e:

            print("Keyword Error:", e)

            return ["AI", "Technology"]