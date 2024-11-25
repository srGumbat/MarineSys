from flask import Flask, render_template, request, send_file
import pandas as pd
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/draft-survey', methods=['POST'])
def draft_survey():
    data = request.form['data']  # Recebe os dados do formulário
    # Aqui você processaria os dados enviados (simulado por enquanto)
    
    # Criar um PDF temporário
    pdf_path = "draft_survey_report.pdf"
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Draft Survey Report")
    c.drawString(100, 730, f"Dados recebidos: {data[:50]}...")  # Exemplo de texto no PDF
    c.save()
    
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
