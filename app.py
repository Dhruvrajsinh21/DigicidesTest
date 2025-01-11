from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Dhruv%40251103@localhost:5432/farmer'


db = SQLAlchemy(app)

class farmerinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    PINcode = db.Column(db.String(6), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/info', methods=['POST'])
def post_info():
    data = request.get_json()
    new_data = farmerinfo(name = data['name'], location = data.get('location'), number = data.get('number'), PINcode = data.get('PINcode'))
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message":"post successfully"})



if __name__ == '__main__':
    app.run()    