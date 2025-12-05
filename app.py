from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMULA_FILE = os.path.join(BASE_DIR, "formulas.json")

with open(FORMULA_FILE, "r", encoding="utf-8") as f:
    FORMULAS = json.load(f)

@app.route("/")
def home():
    return "<h1>GATE Maths Formula API</h1>"

@app.route("/topics")
def topics():
    t = sorted(list({item["topic"] for item in FORMULAS}))
    return jsonify(t)

@app.route("/formulas")
def formulas():
    topic = request.args.get("topic")
    if topic:
        filtered = [x for x in FORMULAS if x["topic"].lower() == topic.lower()]
        return jsonify(filtered)
    return jsonify(FORMULAS)

@app.route("/search")
def search():
    q = request.args.get("q", "").lower()
    results = []
    for f in FORMULAS:
        combined = f["name"] + f["formula"] + f.get("note", "")
        if q in combined.lower():
            results.append(f)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
