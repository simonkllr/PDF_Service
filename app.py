from flask import Flask, request, send_file
from weasyprint import HTML
import tempfile
import os

app = Flask(__name__)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.json
    html_content = data.get('html', '')

    # Temporäre Datei für PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
        pdf_path = tmp.name
    HTML(string=html_content).write_pdf(pdf_path)

    return send_file(pdf_path, as_attachment=True, download_name='output.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
