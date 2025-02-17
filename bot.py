from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip().lower()
    response = MessagingResponse()
    msg = response.message()

    if "saranathan" in incoming_msg:
        msg.body(
            "Here are the details about Saranathan College of Engineering:\n"
            "Departments: CSE, ECE, EEE, MECH, IT, ICE, Civil, AID, AIML, CSBS\n"
            "Tuition Fee per Year:\n"
            "  - Accredited Courses (CSE, ECE, EEE, IT, ICE, MECH): ₹60,000\n"
            "  - Other Courses (Civil, AID, AIML, CSBS): ₹55,000\n"
            "Additional Fees:\n"
            "  - Admission Fee (One-Time): ₹5,000\n"
            "  - Establishment Charges (One-Time): ₹5,000\n"
            "  - Room Rent (Monthly): ₹2,080\n"
            "  - Mess Bill (Monthly): ₹4,580\n"
            "  - Electricity Charges (Yearly): ₹5,000\n"
            "  - Transport Charges (Yearly): ₹15,000\n"
            "Scholarships: Available based on merit.\n"
            "For further details: https://saranathan.ac.in"
        )

    elif "krce" in incoming_msg or "k ramakrishna" in incoming_msg:
        msg.body(
            "Here are the details about K. Ramakrishnan College of Engineering:\n"
            "Departments: CSE, EEE, ECE, MECH, AI & DS, CSE (AI & ML), IT, CSBS\n"
            "Tuition Fee for B.E. in Computer Science and Engineering (4 years): ₹2,00,000\n"
            "  - This equates to ₹50,000 per year.\n"
            "Additional Fees:\n"
            "  - Admission Fee (One-Time): ₹1,000\n"
            "  - Room Rent (Yearly): ₹30,000\n"
            "  - Electricity Charges (Monthly): ₹200\n"
            "  - Mess Bill (Monthly): ₹5,000\n"
            "  - Transport Charges (Yearly): ₹17,000\n"
            "Scholarships: Available.\n"
            "For further details: https://krce.ac.in"
        )

    elif "indra ganesan" in incoming_msg or "igce" in incoming_msg:
        msg.body(
            "Here are the details about Indra Ganesan College of Engineering:\n"
            "Departments: Information not available.\n"
            "Fee: Specific fee details are not publicly available. Please contact the college directly for accurate information.\n"
            "Scholarships: Available.\n"
            "For further details: https://igce.ac.in"
        )

    else:
        msg.body(
            "I can provide information about the following colleges:\n"
            "1. Saranathan College of Engineering\n"
            "2. K. Ramakrishnan College of Engineering\n"
            "3. Indra Ganesan College of Engineering\n"
            "Reply with the college name to get details.\n"
            "For further details: https://yourwebsite.com"
        )

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
