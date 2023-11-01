from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Function to estimate crack time based on password complexity
def estimate_crack_time(password):
    # Calculate complexity score based on password length and character types
    length_score = len(password) / 8
    lower_score = 0 if not any(c.islower() for c in password) else 1
    upper_score = 0 if not any(c.isupper() for c in password) else 1.5
    digit_score = 0 if not any(c.isdigit() for c in password) else 2
    symbol_score = 0 if not any(c in '!@#$%^&*()_+[]{}|;:,.<>?/~`"\'\\' for c in password) else 2.5
    complexity_score = length_score + lower_score + upper_score + digit_score + symbol_score

    # Estimated time in seconds (adjust the constants as needed)
    average_crack_time = 0.029  # Average time to crack one password attempt in seconds
    if len(password)<=5:
        estimated_time_seconds = (math.pow(2, complexity_score) / average_crack_time) * 2
    else:
        estimated_time_seconds = (math.pow(2, complexity_score) / average_crack_time) * 3

    return estimated_time_seconds

@app.route('/', methods=['GET', 'POST'])
def estimate_crack_time_page():
    password = ""
    estimated_time_seconds = None

    if request.method == 'POST':
        password = request.form.get('password', '')
        estimated_time_seconds = estimate_crack_time(password)

    return render_template('index.html', password=password, estimated_time_seconds=estimated_time_seconds)

if __name__ == '__main__':
    app.run()
