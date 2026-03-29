from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# เก็บข้อมูลคำขอ (แบบง่าย)
requests_db = []

@app.route('/')
def home():
    # หน้าแรกต้องเรียกไฟล์ form.html
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
    if id < len(requests_db):
        req = requests_db[id]
        req[role] = decision
    return redirect(url_for('status'))

if __name__ == '__main__':
    # ตั้งค่าให้รองรับ Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
