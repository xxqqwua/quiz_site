from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import random
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def connect_to_db():
    connect = sqlite3.connect('test.db')
    
    return connect

@app.route('/')
def index():  # view
    connect = connect_to_db()
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute("select * from quiz")
    quizes = cursor.fetchall()
    # return "<h1>Hello, world!<h1>"
    session['correct_answer'] = 0
    session['current_question'] = 0
    session['all_questions'] = []
    session['count_questions'] = 0
    session['right_answer'] = ''
    # print(session['correct_answer'])
    template = render_template('index.html', quizes=quizes)
    return template

@app.route('/quiz/', methods=['GET', 'POST'])
def quiz(): 
    if request.method == 'GET':
        id = request.args.get('id')
        if id:
            connect = connect_to_db()
            cursor = connect.cursor()
            cursor.execute("""
                SELECT 
                questions.id,
                questions.question, 
                questions.right_answer,
                questions.wrong_answer1, 
                questions.wrong_answer2, 
                questions.wrong_answer3
                FROM quiz_questions, questions
                WHERE quiz_questions.id_quiz == (?)
                AND questions.id == quiz_questions.id_question
            """, [id])
            session['all_questions'] = cursor.fetchall()
            session['count_questions'] = len(session['all_questions'])
            current_quest = session['current_question']
            all_quest = session['all_questions']
            quest = list(all_quest[current_quest])
            session['right_answer'] = quest[2]
            question = quest[1]
            answers = quest[2:6]
            random.shuffle(answers)
            return render_template("test.html", question=question, answers=answers)
    
    elif request.method == 'POST':
        print(request.form)
        answer = request.form.get("answer")
        if session['current_question'] < session['count_questions'] - 1:
            session['current_question'] += 1
        else:
            # return redirect("http://localhost:5000/result")
            return redirect(url_for("result"))
        if answer == session['right_answer']:
            session['correct_answer'] += 1
            # return "Вы ответили верно"
        current_quest = session['current_question']
        all_quest = session['all_questions']
        quest = list(all_quest[current_quest])
        session['right_answer'] = quest[2]
        question = quest[1]
        answers = quest[2:6]
        random.shuffle(answers)
        return render_template("test.html", question=question, answers=answers)
        

@app.route('/result')
def result():  
    return f"Вы сделали {session['correct_answer']} правильных ответов из {session['count_questions']}"

app.run(debug=True)

