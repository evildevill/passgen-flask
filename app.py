from flask import Flask, render_template, request, jsonify, send_from_directory
import random
import string
import os

app = Flask(__name__)

@app.route('/manifest.json')
def manifest():
    return send_from_directory(os.getcwd(), 'manifest.json')

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True, exclude_similar_chars=False):
    characters = ''
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if exclude_similar_chars:
        characters = ''.join(char for char in characters if char not in 'iIlLoO10')

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        include_uppercase = 'include_uppercase' in request.form
        include_lowercase = 'include_lowercase' in request.form
        include_digits = 'include_digits' in request.form
        include_special_chars = 'include_special_chars' in request.form

        generated_password = generate_password(
            length=password_length,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase,
            include_digits=include_digits,
            include_special_chars=include_special_chars
        )
        return render_template('index.html', generated_password=generated_password)

    return render_template('index.html', generated_password=None)


# New API endpoint for password generation
@app.route('/api/generate-password', methods=['GET'])
def api_generate_password():
    # Get parameters from query string
    length = int(request.args.get('length', 14))
    include_uppercase = request.args.get('include_uppercase', 'true').lower() == 'true'
    include_lowercase = request.args.get('include_lowercase', 'true').lower() == 'true'
    include_digits = request.args.get('include_digits', 'true').lower() == 'true'
    include_special_chars = request.args.get('include_special_chars', 'true').lower() == 'true'
    exclude_similar_chars = request.args.get('exclude_similar_chars', 'false').lower() == 'true'

    generated_password = generate_password(
        length=length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_digits=include_digits,
        include_special_chars=include_special_chars,
        exclude_similar_chars=exclude_similar_chars
    )

    # Return generated password as JSON
    return jsonify({'generated_password': generated_password})


if __name__ == '__main__':
    app.run(debug=True)