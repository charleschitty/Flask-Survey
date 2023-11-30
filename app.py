from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def index():
    """..."""

    return render_template("survey_start.html",
                            survey = survey.title,
                            survey_instructions = survey.instructions)

@app.post('/begin')
def get_survey():
    """..."""

    questions = [question for question in survey.questions]
    print(questions)

    return render_template("question.html", questions = questions)


#Questions: Why Post  vs. Get


# @app.post('/begin')
# def post_survey():



#responses --> empty list
#keeps track of user's survey responses

#user answers questions --> store answers responses list (currently empty)
#ex: ['Yes', 'No', 'Less than $10,000', 'Yes']


#Root Route
#Render page that shows tilte of survey, instructions, and button to start survey
#button redirects user to /questsions/0