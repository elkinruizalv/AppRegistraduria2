from flask import Flask

from routes.stations import stations_bp
from routes.partidos import partidos_bp
from routes.candidates import candidates_bp
from routes.votes import votes_bp

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "Server running..."
    })




if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)