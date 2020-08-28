from flask import Flask, render_template
from data import scrape_poll_data

app = Flask(__name__) #four underscores total

@app.route('/')
def presidential_poll_dashboard():
    pollster_data_array = scrape_poll_data()
    # The pollster_data_array on the left is a variable which can be accessed inside home.html
    # The pollster_data_array on the right is the array created by the scrape_poll_data function
    return render_template('home.html', pollster_data_array = pollster_data_array)

if __name__ == '__main__':
    app.run()