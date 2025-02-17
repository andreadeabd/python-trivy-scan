from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Andrea De la fuente Abdelkader 1ºC_B Curso 2024/2025'

if __name__ == "__main__":
    app.run(debug=True)
