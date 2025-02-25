from flask import Flask, render_template
import os
from utils import extract_paper_details

app = Flask(__name__)

PAPERS_FOLDER = "papers"

def get_papers():
    papers = []
    for filename in os.listdir(PAPERS_FOLDER):
        if filename.endswith(".docx"):
            paper_details = extract_paper_details(os.path.join(PAPERS_FOLDER, filename))
            papers.append({"name": filename, **paper_details})
    return papers

@app.route('/')
def home():
    papers = get_papers()
    return render_template('index.html', papers=papers)

@app.route('/paper/<filename>')
def view_paper(filename):
    paper_details = extract_paper_details(os.path.join(PAPERS_FOLDER, filename))
    return render_template('paper.html', **paper_details)

if __name__ == '__main__':
    app.run(debug=True)
