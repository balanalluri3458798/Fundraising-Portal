from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/",methods=["GET"])
def get_user():
    data = {
        "name": "Balakumari",
        "referral_code": "balakumari2025",
        "donation_amount": 5200
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
