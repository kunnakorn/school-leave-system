from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

requests_db = []

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    student_name = request.form['name']
    reason = request.form['reason']

    data = {
        'id': len(requests_db),
        'name': student_name,
        'reason': reason,
        'parent': None,
        'teacher': None,
        'head': None
    }

    requests_db.append(data)

    return redirect(url_for('status'))

@app.route('/status')
def status():
    return render_template('status.html', requests=requests_db)

@app.route('/approve/<int:id>/<role>/<decision>')
def approve(id, role, decision):
    req = requests_db[id]
    req[role] = decision
    return redirect(url_for('status'))

if __name__ == '__main__':
    app.run(debug=True)