from flask import Flask, render_template

app = Flask(__name__)  # Gunakan __name__ sebagai argumen untuk Flask

@app.route("/")
def home():
    return render_template("index.html")  # Pastikan file index.html ada di folder templates

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Tambahkan host="0.0.0.0"
