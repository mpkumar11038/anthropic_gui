from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    print("Index page accessed.")
    return render_template("index.html")

@app.route("/yes", methods=["POST"])
def yes():
    print("✅ YES button clicked successfully!")
    return jsonify({"message": "✅ YES button clicked successfully!"})

@app.route("/no", methods=["POST"])
def no():
    print("❌ NO button clicked successfully!")
    return jsonify({"message": "❌ NO button clicked successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
