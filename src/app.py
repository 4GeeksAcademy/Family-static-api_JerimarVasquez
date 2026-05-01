from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
CORS(app)

# Inicializar familia Jackson
jackson_family = FamilyStructure("Jackson")

# GET /members


@app.route("/members", methods=["GET"])
def get_all_members():
    try:
        return jsonify(jackson_family.get_all_members()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /members/<id>


@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /members


@app.route("/members", methods=["POST"])
def add_member():
    try:
        body = request.get_json()
        if not body:
            return jsonify({"error": "Invalid JSON"}), 400

        new_member = jackson_family.add_member(body)
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE /members/<id>


@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    try:
        deleted = jackson_family.delete_member(member_id)
        if deleted:
            return jsonify({"done": True}), 200
        return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

