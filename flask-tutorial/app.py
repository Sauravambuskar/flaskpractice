from flask import Flask

# Create a Flask application instance its a app = Flask(__name__) its meaning the name of the current module
app = Flask(__name__)


@app.route('/')  # Define a route for the root URL
def home():

    return "Hello, Flasoo xxxx gurss !"  # Return a simple response for the root URL


if __name__ == '__main__':  # Check if the script is run directly

    # Run the Flask application in debug mode here True means enable debug mode false means disable debug mode if the debugs mode is enabled the server will automatically reload for code changes and provide a debugger in case of an error       
    app.run(debug=True)
