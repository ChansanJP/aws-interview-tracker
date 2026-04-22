from flask import Flask, request

app = Flask(__name__)

applications = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        company = request.form.get("company")
        status = request.form.get("status")

        if company and status:
            applications.append({"company": company, "status": status})

    items = ""
    for item in applications:
        items += f"<li><strong>{item['company']}</strong> - {item['status']}</li>"

    return f"""
    <h1>AWS Interview Tracker</h1>
    <p>Add a company and status below.</p>

    <form method="POST">
        <input type="text" name="company" placeholder="Enter company name">
        <select name="status">
            <option value="Applied">Applied</option>
            <option value="Interview">Interview</option>
            <option value="Rejected">Rejected</option>
            <option value="Offer">Offer</option>
        </select>
        <button type="submit">Add</button>
    </form>

    <h2>Applications</h2>
    <ul>
        {items}
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
