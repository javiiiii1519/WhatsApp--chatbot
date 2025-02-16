from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Sample college data
college_data = {
    "Saranathan College of Engineering": {
        "Departments": "CSE, ECE, MECH, CIVIL, IT",
        "Fee": "Rs. 75,000 per year",
        "Scholarship": "Merit-based scholarships available",
        "Location": "Trichy, Tamil Nadu",
        "Hostel": "Yes, Rs. 50,000 per year",
        "Bus Facility": "Yes, Rs. 15,000 per year",
        "Timing": "8:30 AM - 4:30 PM",
        "Dress Code": "Formal with shoes"
    },
    "K Ramakrishna College of Engineering": {
        "Departments": "CSE, AI&DS, EEE, MECH, CIVIL",
        "Fee": "Rs. 70,000 per year",
        "Scholarship": "Based on entrance exam scores",
        "Location": "Trichy, Tamil Nadu",
        "Hostel": "Yes, Rs. 48,000 per year",
        "Bus Facility": "Yes, Rs. 12,000 per year",
        "Timing": "9:00 AM - 5:00 PM",
        "Dress Code": "Casual on Fridays"
    },
    "Indra Ganesan College of Engineering": {
        "Departments": "CSE, ECE, BIOTECH, MECH",
        "Fee": "Rs. 68,000 per year",
        "Scholarship": "For top 10 rank holders",
        "Location": "Trichy, Tamil Nadu",
        "Hostel": "Yes, Rs. 55,000 per year",
        "Bus Facility": "Yes, Rs. 10,000 per year",
        "Timing": "8:00 AM - 4:00 PM",
        "Dress Code": "Uniform compulsory"
    }
}

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").strip()
    response = MessagingResponse()

    if incoming_msg in college_data:
        details = "\n".join([f"{key}: {value}" for key, value in college_data[incoming_msg].items()])
        response.message(f"Here are the details for {incoming_msg}:\n{details}")
    else:
        response.message("Please select a valid college: Saranathan College of Engineering, K Ramakrishna College of Engineering, Indra Ganesan College of Engineering")

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
