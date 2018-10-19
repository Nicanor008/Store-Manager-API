import os
from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app()

app.route('/')
def index():
    return "<h1> Welcome to Nicanor Store Manager</h1>"

if __name__ == '__main__':
    app.run(debug=True)