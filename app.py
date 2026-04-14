from flask import Flask, render_template, request, jsonify
import re
import math

app = Flask(__name__)

def calculate_entropy(password):
    charset = 0
    if re.search("[a-z]", password): charset += 26
    if re.search("[A-Z]", password): charset += 26
    if re.search("[0-9]", password): charset += 10
    if re.search("[!@#$%^&*()_+=-]", password): charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search("[!@#$%^&*()_+=-]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    entropy = calculate_entropy(password)

    return score, feedback, entropy

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    password = data['password']

    score, feedback, entropy = check_strength(password)

    return jsonify({
        "score": score,
        "feedback": feedback,
        "entropy": entropy
    })

if __name__ == '__main__':
    app.run(debug=True)
    