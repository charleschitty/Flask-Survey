from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def index(): #survey_start() show_survey_start() might be better
    """Renders start of survey with survey name and instructions"""

    return render_template("survey_start.html",
                            survey=survey.title,
                            survey_instructions=survey.instructions)

@app.post("/begin")
def redirect_to_first_question():
    """From the survey start, redirect from /begin to first survey question"""

    responses.clear() # clears the responses everytime we start a new survey

    return redirect("/question/0")

@app.get('/question/<int:id>') #change to something more specific like question_id
def get_question(id):
    """Renders the HTML for each survey question"""
    print("id", id)

    question = survey.questions[id]

    return render_template(
        "question.html",
        question=question,
        id=id
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
    responses.append(answer)

    id = int(request.form["id"])
    new_id = id + 1

    questions = survey.questions


    print("responses", responses)

    if new_id < len(survey.questions): # if length of responses = length of questions then cool! if not, redirect to correct q
        return redirect(f"/question/{new_id}") #len(responses) instead of new_id
    else:
        return render_template("completion.html", # see line 36–39 and copy style
                               questions=questions,
                               responses=responses) #remove spaces between =