# app.py

from flask import (
    Flask,
    jsonify,
    request,
    render_template
)

from flask_cors import CORS

from core.headline_engine import HeadlineEngine

app = Flask(__name__)

CORS(app)

engine = HeadlineEngine()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/health")
def health():

    return jsonify({

        "status": "healthy",

        "project": "HeadlineIQ AI"
    })


@app.route("/generate", methods=["POST"])
def generate():

    try:

        if not request.is_json:

            return jsonify({

                "success": False,

                "message": "Request must be JSON"

            }), 400

        data = request.get_json()

        if not data:

            return jsonify({

                "success": False,

                "message": "No data received"

            }), 400

        text = str(
            data.get("text", "")
        ).strip()

        style = str(
            data.get(
                "style",
                "professional"
            )
        ).strip()

        total = int(
            data.get("total", 6)
        )

        if len(text) < 50:

            return jsonify({

                "success": False,

                "message":
                "Please enter at least 50 characters"

            }), 400

        result = engine.synthesize_headlines(

            text=text,

            style=style,

            total=total
        )

        if not result:

            return jsonify({

                "success": False,

                "message":
                "Headline generation failed"

            }), 500

        return jsonify({

            "success": True,

            "data": result
        })

    except Exception as e:

        print("\n" + "=" * 60)
        print("BACKEND ERROR:")
        print(str(e))
        print("=" * 60 + "\n")

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500


if __name__ == "__main__":

    print("\n" + "=" * 60)

    print("🧠 HeadlineIQ AI Starting...")

    print("=" * 60)

    print("✓ Flask Server Loaded")

    print("✓ NLP Engines Loaded")

    print("✓ Sentiment Engine Active")

    print("✓ Entity Recognition Ready")

    print("✓ Headline Synthesis Online")

    print("=" * 60)

    print("🌐 Running on:")
    print("http://127.0.0.1:5000")

    print("=" * 60 + "\n")

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000
    )