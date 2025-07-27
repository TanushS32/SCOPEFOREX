from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("home.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Forex Services Page
@app.route("/forex-services")
def forex_services():
    return render_template("forex-services.html")

# Financial Services Page
@app.route("/financial-services")
def financial_services():
    return render_template("financial-services.html")

# FAQs Page
@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Sitemap route
@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")

# Favicon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
