from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/zl2474')
def zl2474():
    return render_template('zl2474.html')


if __name__ == '__main__':
    app.run()