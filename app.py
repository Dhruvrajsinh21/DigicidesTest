from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dhruv%40251103@localhost:5432/farmer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class farmerInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(10), unique=True, nullable=False)
    PINcode = db.Column(db.String(6), nullable=False)

@app.route('/info', methods=['POST'])
def post_info():
    try:
        data = request.get_json()
        if not data.get('name') or not data.get('number') or not data.get('PINcode'):
            return jsonify({"error": "Missing required fields (name, number, PINcode)."}), 400
        new_farmer = farmerInfo(
            name=data['name'],
            location=data.get('location', ''),
            number=data['number'],
            PINcode=data['PINcode']
        )
        db.session.add(new_farmer)
        db.session.commit()

        return jsonify({"message": "Farmer added successfully."}), 201

    except Exception as e:
        db.session.rollback()
        if "unique constraint" in str(e):
            return jsonify({"error": "Phone number must be unique."}), 400
        return jsonify({"error": "An error occurred: " + str(e)}), 500

@app.route('/info', methods=['GET'])
@app.route('/info/<int:farmer_id>', methods=['GET'])
def get_info(farmer_id=None):
    try:
        if farmer_id is not None:
            farmer = farmerInfo.query.get(farmer_id)
            if not farmer:
                return jsonify({"error": f"Farmer with ID {farmer_id} not found."}), 404
            return jsonify({
                "id": farmer.id,
                "name": farmer.name,
                "location": farmer.location,
                "number": farmer.number,
                "PINcode": farmer.PINcode
            }), 200

        farmers = farmerInfo.query.all()
        return jsonify([
            {
                "id": farmer.id,
                "name": farmer.name,
                "location": farmer.location,
                "number": farmer.number,
                "PINcode": farmer.PINcode
            } for farmer in farmers
        ]), 200

    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)}), 500


if __name__ == '__main__':
    app.run()
