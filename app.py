from flask import Flask, render_template, send_from_directory, Response
import datetime

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

# Favicon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")

# Dynamic Sitemap.xml
@app.route("/sitemap.xml")
def sitemap():
    pages = [
        {"loc": "https://www.scopeforex.in/", "priority": "1.0", "changefreq": "daily"},
        {"loc": "https://www.scopeforex.in/forex-services", "priority": "0.9", "changefreq": "weekly"},
        {"loc": "https://www.scopeforex.in/financial-services", "priority": "0.8", "changefreq": "weekly"},
        {"loc": "https://www.scopeforex.in/faqs", "priority": "0.6", "changefreq": "monthly"},
        {"loc": "https://www.scopeforex.in/contact", "priority": "0.6", "changefreq": "monthly"},
    ]
    lastmod = datetime.datetime.utcnow().date().isoformat()
    return render_template("sitemap.xml", pages=pages, lastmod=lastmod), 200, {'Content-Type': 'application/xml'}

# robots.txt
@app.route("/robots.txt")
def robots_txt():
    content = """User-agent: *
Disallow:

Sitemap: https://www.scopeforex.in/sitemap.xml
"""
    return Response(content, mimetype='text/plain')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
