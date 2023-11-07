from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_random_number', methods=['POST'])
def generate_random_number():
    if request.method == 'POST':
        random_number = random.randint(1, 100)
        return str(random_number)


if __name__ == '__main__':
    app.run(debug=True)
