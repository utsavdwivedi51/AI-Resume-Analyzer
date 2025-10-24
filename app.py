from flask import Flask, render_template, request
from resume_parser import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    if request.method == "POST":
        resume_text = request.form["resume"]
        job_text = request.form["job"]
        score, insights = analyze_resume(resume_text, job_text)
        return render_template("index.html", score=score, insights=insights)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
