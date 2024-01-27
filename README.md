# Password Generator API

This is a simple Flask-based Password Generator API with added features for customization. The API allows you to generate strong passwords with various options such as length, including or excluding uppercase letters, lowercase letters, digits, special characters, and excluding similar characters.

## Base URL

- [https://passgen-flask.vercel.app/](https://passgen-flask.vercel.app/)

## API Endpoints

### 1. Password Generation

#### Endpoint: `/api/generate-password`

This endpoint generates a random password based on specified parameters.

#### Parameters:

- `length` (optional, default: 14): Length of the password.
- `include_uppercase` (optional, default: true): Include uppercase letters.
- `include_lowercase` (optional, default: true): Include lowercase letters.
- `include_digits` (optional, default: true): Include digits.
- `include_special_chars` (optional, default: true): Include special characters.
- `exclude_similar_chars` (optional, default: false): Exclude similar characters.

#### Example Usage:

```bash
# Generate a password with default settings (length=14, include all)
curl --request GET \
	--url https://securepassgen-api-ultimate-online-password-generator.p.rapidapi.com/api/generate-password \
	--header 'X-RapidAPI-Host: securepassgen-api-ultimate-online-password-generator.p.rapidapi.com' \
	--header 'X-RapidAPI-Key: YOUR_API_KEY'

# Generate a password with custom settings
curl --request GET \
	--url https://securepassgen-api-ultimate-online-password-generator.p.rapidapi.com/api/generate-password?length=16&include_uppercase=true&include_digits=true&exclude_similar_chars=true \
	--header 'X-RapidAPI-Host: securepassgen-api-ultimate-online-password-generator.p.rapidapi.com' \
	--header 'X-RapidAPI-Key: YOUR_API_KEY'
```

```python
# Generate a password with default settings (length=14, include all)
import requests

url = "https://securepassgen-api-ultimate-online-password-generator.p.rapidapi.com/api/generate-password"

headers = {
	"X-RapidAPI-Key": "YOUR_API_KEY",
	"X-RapidAPI-Host": "securepassgen-api-ultimate-online-password-generator.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
// Generate a password with default settings (length=14, include all)
var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://securepassgen-api-ultimate-online-password-generator.p.rapidapi.com/api/generate-password",
    "method": "GET",
    "headers": {
        "X-RapidAPI-Host": "securepassgen-api-ultimate-online-password-generator.p.rapidapi.com",
        "X-RapidAPI-Key": "YOUR_API_KEY"
    }
}
```

### 2. Password Generation via a Web interface

#### Endpoint: `/`

This is the web interface for password generation. You can visit  [https://passgen-flask.vercel.app/](https://passgen-flask.vercel.app/) and use the provided form to generate passwords with various options.

### Local Setup (Optional)

If you want to run the Flask app locally, follow these steps:

0. Clone the repository:

```bash
git clone https://github.com/evildevill/passgen-flask.git
```

1. Change the directory:

```bash
cd passgen-flask
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the web interface


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.