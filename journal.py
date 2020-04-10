from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/jobs.sqlite')


@app.route('/')
def show_journal():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('journal.html', jobs=jobs)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
