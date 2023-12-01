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

@app.post("/begin")
def redirect_to_first_question():
    """. . . """
    # From the survey start, redirect from /begin to first question

    return redirect("/question/0")

@app.get('/question/<int:id>')
def get_survey(id):
    """..."""
    print("id", id)

    # We want to "stop" this eventually so set if length of responses = length of survey.questions
    # Redirect to the thank you page and flash

    question = survey.questions[id]

    return render_template("question.html", question = question, id = id)

@app.post('/answer')
def redirect_to_next_question():
    """..."""

    answer = request.form["answer"]
    id = int(request.form["id"])
    new_id = id + 1
    responses.append(answer)


    #(answer, value) dict
    print(responses)

    if new_id < :
        return redirect(f"/question/{new_id}")
    else:
        return redirect("completion.html", responses = responses)


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