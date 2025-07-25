from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/forex-services")
def forex_services():
    return render_template("forex-services.html")

@app.route("/financial-services")
def financial_services():
    return render_template("financial-services.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

