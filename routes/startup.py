from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from agents.orchestrator import run_startup_simulator

startup_bp = Blueprint("startup", __name__)


@startup_bp.route("/generate", methods=["POST"])
@jwt_required()
def generate():

    data = request.get_json()

    idea = data.get("idea")

    # Get selected agents
    selected_agents = data.get("agents")

    # If frontend sends [] or nothing, use all agents
    if not selected_agents:
        selected_agents = [
            "CEO",
            "Marketing",
            "Sales",
            "HR",
            "Finance"
        ]

    if not idea:
        return jsonify({
            "message": "Business idea is required."
        }), 400

    print("Idea:", idea)
    print("Agents:", selected_agents)
    print("User:", get_jwt_identity())

    result = run_startup_simulator(
        idea,
        selected_agents
    )

    print("Result:", result)

    return jsonify(result), 200