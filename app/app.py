from flask import Flask, render_template_string, request

app = Flask(__name__)

votes = {"Python": 0, "Java": 0, "Go": 0}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Polling App</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h2>Vote for your favorite language!</h2>
    <form method="POST">
        {% for lang in votes %}
            <button type="submit" name="choice" value="{{ lang }}">{{ lang }}</button>
        {% endfor %}
    </form>
    <h3>Current Results:</h3>
    <ul style="list-style:none;">
        {% for lang, count in votes.items() %}
            <li>{{ lang }} : {{ count }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice in votes:
            votes[choice] += 1
    return render_template_string(HTML, votes=votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
