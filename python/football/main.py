from flask import Flask, render_template
from setup import Team, setup_groups


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', groups=groups)


if __name__ == '__main__':
    groups: dict[str, list[Team]] = setup_groups()
    app.run(debug=True)
