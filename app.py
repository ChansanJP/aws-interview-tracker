from flask import Flask, request

app = Flask(__name__)

applications = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        company = request.form.get("company")
        status = request.form.get("status")
        notes = request.form.get("notes", "").strip()

        if company and status:
            applications.append({
                "company": company,
                "status": status,
                "notes": notes
            })

    items = ""
    for item in applications:
        notes_html = f"<br><small>{item['notes']}</small>" if item["notes"] else ""
        items += f"<li><strong>{item['company']}</strong> - {item['status']}{notes_html}</li><br>"

    return f"""
    <h1>AWS Interview Tracker</h1>
    <p>Add a company, status, and notes below.</p>

    <form method="POST">
        <input type="text" name="company" placeholder="Enter company name">
        <select name="status">
            <option value="Applied">Applied</option>
            <option value="Interview">Interview</option>
            <option value="Rejected">Rejected</option>
            <option value="Offer">Offer</option>
        </select>
        <br><br>
        <textarea name="notes" placeholder="Enter notes" rows="4" cols="40"></textarea>
        <br><br>
        <button type="submit">Add</button>
    </form>

    <h2>Applications</h2>
    <ul>
        {items}
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
