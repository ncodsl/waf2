<<<<<<< HEAD
from website import create_app

app = create_app()

# Remove the if __name__ == '__main__' block for Vercel deployment
# Instead, just export the app variable


=======
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
>>>>>>> 9fba82ef4eb60f6de55fbb2bd547d6dd993094eb
