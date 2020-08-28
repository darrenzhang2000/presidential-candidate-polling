from flask import Flask

app = Flask(__name__) #four underscores total

@app.route('/')
def presidential_poll_dashboard():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()