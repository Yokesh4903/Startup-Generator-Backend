from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from agents.orchestrator import run_startup_simulator
from database.mongo import history

startup_bp = Blueprint("startup", __name__)


@startup_bp.route("/generate", methods=["POST"])
@jwt_required()
def generate():

    data = request.get_json()

    idea = data.get("idea")
    selected_agents = data.get("agents", [])

    if not idea:
        return jsonify({
            "message": "Business idea is required."
        }), 400

    # Run AI agents
    result = run_startup_simulator(
        idea,
        selected_agents
    )

    # MongoDB user id from JWT
    user_id = get_jwt_identity()

    # Save history in MongoDB
    history.insert_one({
        "user_id": user_id,
        "idea": idea,
        "ceo": result.get("CEO", ""),
        "marketing": result.get("Marketing", ""),
        "sales": result.get("Sales", ""),
        "hr": result.get("HR", ""),
        "finance": result.get("Finance", "")
    })

    return jsonify(result), 200