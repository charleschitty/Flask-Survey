from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.get("/")
def survey_start():
    """Renders start of survey with survey name and instructions"""

    session["responses"] = []

    return render_template("survey_start.html",
                            survey=survey)

@app.post("/begin")
def redirect_to_first_question():
    """From the survey start, redirect from /begin to first survey question"""

    session["responses"].clear()

    return redirect("/question/0")


@app.get('/question/<int:question_id>')
def get_question(question_id):
    """Renders the HTML for each survey question"""

    responses_length = len(session["responses"])

    if responses_length == len(survey.questions):
        return render_template(
            "completion.html",
            questions=survey.questions,
            responses=session["responses"])

    if question_id != responses_length:
        flash(
            f"""
            Failed to access question {question_id}!
            You are on question {responses_length}.
            """
        )
        return redirect(f"/question/{len(session['responses'])}")

    question = survey.questions[responses_length]

    return render_template(
        "question.html",
        question=question,
        id=question_id
    )



@app.post('/answer')
def handle_question_submission():
    """
    Checks to see if next question id is within the range of survey questions
    If within range, redirects to next question
    If outside range, ends survey and loads completion page with survey
    question responses
    """

    answer = request.form["answer"]

    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses

    if len(session["responses"]) == len(survey.questions):
        return render_template(
            "completion.html",
            questions=survey.questions,
            responses=session["responses"])
    else:
        return redirect(f"/question/{len(session['responses'])}")
