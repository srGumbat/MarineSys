from flask import Flask, render_template, request, send_file
import pandas as pd
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo ao MARINESYS! Sistema em desenvolvimento."

@app.route('/draft-survey', methods=['POST'])
def draft_survey():
    # Aqui você pode adicionar os cálculos do Draft Survey
    # Por exemplo, processar os dados recebidos e criar o PDF
    pdf_path = "draft_survey_report.pdf"
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Draft Survey Report")
    c.save()
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
