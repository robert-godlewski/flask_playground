from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world(): return render_template('index.html')

@app.route('/play')
def play_default(): return render_template('play.html', times=3, color='blue')

@app.route('/play/<x>')
def play_num(x): 
    max = int(x)
    return render_template('play.html', times=max, color='blue')

@app.route('/play/<x>/<color>')
def play(x, color):
    max=int(x)
    return render_template('play.html', times=max, color=color)


if __name__=="__main__": app.run(debug=True)