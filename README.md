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
curl "https://passgen-flask.vercel.app/api/generate-password"

# Generate a password with custom settings
curl "https://passgen-flask.vercel.app/api/generate-password?length=16&include_uppercase=true&include_digits=true&exclude_similar_chars=true"
```

### 2. Password Generation via a Web interface

#### Endpoint: `/`

This is the web interface for password generation. You can visit  [https://passgen-flask.vercel.app/](https://passgen-flask.vercel.app/) and use the provided form to generate passwords with various options.
