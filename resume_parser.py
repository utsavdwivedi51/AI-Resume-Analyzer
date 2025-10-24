import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_resume(resume, job):
    resume_doc = nlp(resume)
    job_doc = nlp(job)

    resume_keywords = set([token.lemma_ for token in resume_doc if token.is_alpha])
    job_keywords = set([token.lemma_ for token in job_doc if token.is_alpha])

    match = resume_keywords.intersection(job_keywords)
    score = round(len(match) / len(job_keywords) * 100, 2)

    insights = {
        "matched_keywords": list(match),
        "missing_keywords": list(job_keywords - match)
    }

    return score, insights
