from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'soren'

@app.route('/')
def index():
    if 'count' in session:
        print('key exists!')
        session['count'] += 1
    else:
        session['count'] = 1
        print("key 'count' does NOT exist")
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
