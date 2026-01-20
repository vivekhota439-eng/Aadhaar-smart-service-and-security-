from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

appointments = []
token_number = 1

# Home route -> HTML form
@app.route("/")
def home():
    return render_template("index.html")  # HTML form render karta hai

# Book appointment
@app.route("/book", methods=["POST"])
def book_appointment():
    global token_number
    # Form data read karo
    name = request.form.get("name")
    mobile = request.form.get("mobile")
    service = request.form.get("service")
    date = request.form.get("date")

    appointment = {
        "token": token_number,
        "name": name,
        "mobile": mobile,
        "service": service,
        "date": date,
        "time": datetime.now().strftime("%H:%M:%S")
    }

    appointments.append(appointment)
    token_number += 1

    return f"Appointment booked successfully! Your token number is {appointment['token']}"

# All appointments
@app.route("/tokens", methods=["GET"])
def get_tokens():
    return jsonify(appointments)

if __name__ == "__main__":
    app.run(debug=True)
