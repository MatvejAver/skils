#Импорт
from flask import Flask, render_template,request, redirect
import datetime



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    text = request.form['text']
    time = datetime.datetime.now()
    time_res = f'{time.year}.{time.month}.{time.day} {time.hour}:{time.minute}'

    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(f'{name}\n{email}\n{text}\n{time.year}.{time.month}.{time.day} {time.hour}:{time.minute}.\n\n\n')

    return render_template('form_result.html', email=email, text=text,name=name,time=time_res)


if __name__ == "__main__":
    app.run(debug=True)