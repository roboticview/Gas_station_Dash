Step 1

pip install gunicorn

pip freeze > requirements.txt

Step 2

Create Procfile

In Procfile add

web: gunicorn app:server 

Step 3

Create runtime.txt

Check current Python version supported by DigitalOcean

In runtime.txt add

python-3.9.15

Step 4

In App.py file make sure the app instance is out of function and app is defined outside of any functions and no indentation, add __name__ into Dash()
```
app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
server = app.server
app.layout = create_layout(app, data)

if __name__ == '__main__':
    app.run_server(debug=True)
```

Step 5

Create .gitignore file

In .gitignore add

*.pyc
__pycache__
.DS_Store
venv

Step 6

Push the project to GitHub

Step 7

Create an app on DigitalOcean and autodeploy the project from GitHub repo

Step 8

In DigitalOcean app settings add command

gunicorn --worker-tmp-dir /dev/shm --timeout 120 app:server

