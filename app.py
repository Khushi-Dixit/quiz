from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store quizzes in memory for simplicity (use a database for production)
quizzes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        quiz_title = request.form['quiz_title']
        questions = []
        for i in range(1, int(request.form['total_questions']) + 1):
            question_text = request.form[f'question_{i}']
            options = []
            for j in range(1, int(request.form[f'options_{i}']) + 1):
                option_text = request.form[f'option_{i}_{j}']
                options.append(option_text)
            questions.append({'question': question_text, 'options': options})
        
        quizzes[quiz_title] = questions
        return redirect(url_for('quiz', quiz_title=quiz_title))

    return render_template('create_quiz.html')

@app.route('/quiz/<quiz_title>', methods=['GET', 'POST'])
def quiz(quiz_title):
    if request.method == 'POST':
        # Here you can handle the quiz submission logic
        return redirect(url_for('index'))

    quiz = quizzes.get(quiz_title)
    if not quiz:
        return redirect(url_for('index'))
    
    return render_template('quiz.html', quiz_title=quiz_title, quiz=quiz)

if __name__ == '__main__':
    app.run(debug=True)
