from flask import Flask, render_template
import requests

app = Flask(__name__)

# API URL
api_url = "https://reqres.in/api/users"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user-list')
def user_list():
    # Fetch user data from the API
    response = requests.get(api_url)
    data = response.json()
    
    # Extract user information
    users = data.get("data", [])
    
    # Render the HTML template with user data
    return render_template('user-list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
