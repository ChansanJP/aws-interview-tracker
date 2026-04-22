from flask import Flask, request
import json
import os

app = Flask(__name__)

DATA_FILE = "applications.json"

def load_applications():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_applications(applications):
    with open(DATA_FILE, "w") as file:
        json.dump(applications, file, indent=2)

applications = load_applications()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        company = request.form.get("company", "").strip()
        job_title = request.form.get("job_title", "").strip()
        status = request.form.get("status", "").strip()
        notes = request.form.get("notes", "").strip()

        if company and job_title and status:
            applications.append({
                "company": company,
                "job_title": job_title,
                "status": status,
                "notes": notes
            })
            save_applications(applications)

    items = ""
    for item in applications:
        notes_html = f"<br><small>{item['notes']}</small>" if item["notes"] else ""
        items += f"<li><strong>{item['company']}</strong> - {item['job_title']} - {item['status']}{notes_html}</li><br>"

    return f"""
    <h1>AWS Interview Tracker</h1>
    <p>Add a company, job title, status, and notes below.</p>

    <form method="POST">
        <input type="text" name="company" placeholder="Enter company name">
        <input type="text" name="job_title" placeholder="Enter job title">
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
