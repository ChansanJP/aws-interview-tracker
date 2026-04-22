from flask import Flask, request

app = Flask(__name__)

applications = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        company = request.form.get("company")
        if company:
            applications.append(company)

    items = ""
    for app_name in applications:
        items += f"<li>{app_name}</li>"

    return f"""
    <h1>AWS Interview Tracker</h1>
    <p>Add a company name below.</p>

    <form method="POST">
        <input type="text" name="company" placeholder="Enter company name">
        <button type="submit">Add</button>
    </form>

    <h2>Applications</h2>
    <ul>
        {items}
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
