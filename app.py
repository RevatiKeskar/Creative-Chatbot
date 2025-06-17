from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-8b-latest')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_suggestion', methods=['POST'])
def get_suggestion():
    user_input = request.form['user_input']
    
    try:
        response = model.generate_content(
            f"""You're a creative content assistant. Suggest 3 ideas about: {user_input}
            - Make each suggestion 1-2 sentences
            - Keep tone engaging and practical"""
        )
        return jsonify({'suggestion': response.text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


