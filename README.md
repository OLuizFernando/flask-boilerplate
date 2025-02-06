# Flask Boilerplate

This repository provides a basic boilerplate for web applications built with **Flask**, offering a simple initial structure for development.

The boilerplate uses **Flask** along with **Postgres** (via `psycopg2`), **Bootstrap** for responsive design, and **Vercel** to simplify deployment.

These technologies are entirely optional and can be customized or replaced as needed for your project.

🔗 **Live Demo:** [flask-boilerplate.vercel.app](https://flask-boilerplate.vercel.app)

## Features

- **Flask** for web development
- Optional **Postgres** support with `psycopg2` for **database integration**
- Responsive design with **Bootstrap**
- Simple folder structure for organization
- HTML templates rendered with **Jinja2**
- Pre-built templates for common pages (e.g., login, register, error pages)
- User authentication system with login and registration functionality already implemented
- Easy deployment with Vercel

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/oluizfernando/flask-boilerplate.git
cd flask-boilerplate
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
flask run
```

The application will be available at [`http://127.0.0.1:5000/`](http://127.0.0.1:5000/).

## Configuration Files

### [`.env`](.env)

If your application uses sessions or a database, make sure to fill in the values in the [`.env`](.env) file to configure the database and Flask's secret key. This file should **never** be pushed to a public repository, but it’s essential for both your local development and production environments.

### [`requirements.txt`](requirements.txt)

If you will use a Postgres database, use `psycopg2` for development or only `psycopg2-binary` for production.

### [`.gitignore`](.gitignore)

Make sure to **uncomment** some lines in [`.gitignore`](.gitignore). The files listed are important to ignore, but I have uploaded them for clarity.

### [`vercel.json`](vercel.json)

Modify the [`vercel.json`](vercel.json) file to fit your application structure. It tells Vercel how to build and route your app. You can use the default provided configuration for most Flask apps.

## Deploying to Vercel

You can deploy your application to Vercel using the Vercel CLI. Here’s how to do it:

### 1. Install Vercel CLI

If you don't have Vercel CLI installed, you can install it via npm:

```bash
npm install -g vercel
```

### 2. Log in to Vercel

```bash
vercel login
```

### 3. Deploy the application

```bash
vercel --prod
```

## Project Structure

```
/
|-- static/
|   |-- css/
|   |   |-- custom.css
|   |   |-- style.css
|   |
|   |-- images/
|   |   |-- favicon.ico
|   |   |-- navbar_brand.png
|
|-- templates/
|   |-- errors/
|   |   |-- 404.html
|   |   |-- 405.html
|   |   |-- 500.html
|   |
|   |-- contact.html
|   |-- index.html
|   |-- layout.html
|   |-- login.html
|   |-- register.html
|
|-- .env
|-- .gitignore
|-- app.py
|-- helpers.py
|-- LICENSE
|-- README.md
|-- requirements.txt
|-- vercel.json
```

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for more details.
