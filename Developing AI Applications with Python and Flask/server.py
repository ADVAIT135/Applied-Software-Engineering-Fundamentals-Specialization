from flask import Flask, jsonify, request, make_response
import uuid

app = Flask(__name__)

# Sample data
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    # ... other records ...
]

@app.route("/")
def index():
    return jsonify({"message": "hello world"}), 200

@app.route("/no_content")
def no_content():
    # 204 must not include a body
    return "", 204

@app.route("/exp")
def index_explicit():
    resp = make_response(jsonify({"message": "Hello World"}), 200)
    return resp

@app.route("/data")
def get_data():
    if data:
        return jsonify({"message": f"Data of length {len(data)} found"}), 200
    return jsonify({"message": "Data is empty"}), 500

@app.route("/name_search")
def name_search():
    query = request.args.get("q")

    if query is None:
        return jsonify({"message": "Query parameter 'q' is missing"}), 400
    if query.strip() == "" or query.isdigit():
        return jsonify({"message": "Invalid input parameter"}), 422

    for person in data:
        if query.lower() in person["first_name"].lower() or query.lower() in person["last_name"].lower():
            return jsonify(person), 200

    return jsonify({"message": "Person not found"}), 404

@app.route("/count")
def count():
    return jsonify({"data_count": len(data)}), 200

@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return jsonify(person), 200
    return jsonify({"message": "Person not found"}), 404

@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_person(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return jsonify({"message": "Person with ID deleted"}), 200
    return jsonify({"message": "Person not found"}), 404

@app.route("/person", methods=['POST'])
def create_person():
    new_person = request.get_json()

    if not new_person:
        return jsonify({"message": "Invalid input, no data provided"}), 422
    if "id" not in new_person:
        return jsonify({"message": "Missing 'id' field"}), 422

    # Add to dataset (in-memory for demo)
    data.append(new_person)
    return jsonify({"message": f"Person {new_person['id']} created"}), 201

@app.errorhandler(404)
def api_not_found(error):
    return jsonify({"message": "API not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    # Avoid exposing internal errors
    return jsonify({"message": "Internal server error"}), 500

@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")

if __name__ == "__main__":
    app.run(debug=True)
