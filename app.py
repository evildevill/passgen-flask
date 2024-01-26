from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        include_digits = 'include_digits' in request.form
        include_special_chars = 'include_special_chars' in request.form

        generated_password = generate_password(
            length=password_length,
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
    include_digits = request.args.get('include_digits', 'true').lower() == 'true'
    include_special_chars = request.args.get('include_special_chars', 'true').lower() == 'true'

    generated_password = generate_password(
        length=length,
        include_digits=include_digits,
        include_special_chars=include_special_chars
    )

    # Return generated password as JSON
    return jsonify({'generated_password': generated_password})

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# import random
# import string

# app = Flask(__name__)

# def generate_password(length, include_digits=True, include_special_chars=True):
#     characters = string.ascii_letters
#     if include_digits:
#         characters += string.digits
#     if include_special_chars:
#         characters += string.punctuation

#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         password_length = int(request.form['password_length'])
#         include_digits = 'include_digits' in request.form
#         include_special_chars = 'include_special_chars' in request.form

#         generated_password = generate_password(
#             length=password_length,
#             include_digits=include_digits,
#             include_special_chars=include_special_chars
#         )
#         return render_template('index.html', generated_password=generated_password)

#     return render_template('index.html', generated_password=None)

# # New API endpoint for password generation
# @app.route('/api/generate-password', methods=['GET'])
# def api_generate_password():
#     # Get parameters from query string
#     length = int(request.args.get('length', 14))
#     include_digits = request.args.get('include_digits', 'true').lower() == 'true'
#     include_special_chars = request.args.get('include_special_chars', 'true').lower() == 'true'

#     generated_password = generate_password(
#         length=length,
#         include_digits=include_digits,
#         include_special_chars=include_special_chars
#     )

#     # Return generated password as JSON
#     return jsonify({'generated_password': generated_password})

# if __name__ == '__main__':
#     app.run(debug=True)