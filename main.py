from flask import Flask, request

from testing import TestingParameter  # Ensure this imports correctly

app = Flask(__name__)

@app.route('/landing_page', methods=['GET', 'POST'])
def landing_page():
    if request.method == "POST":
        comment = request.form.get('comment')
        if not comment:
            return "Error: No comment provided", 400  # Handle missing input

        result = TestingParameter(comment).predict()
        return result  # Ensure a valid response is returned

    return "Send a POST request with 'comment' data"  # Handle GET request

if __name__ == "__main__":
    app.run(debug=True)
