from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from agents.orchestrator import run_startup_simulator
from database import db
from database.models import StartupHistory

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
        }),400

    result = run_startup_simulator(
        idea,
        selected_agents
    )

    user_id=int(get_jwt_identity())

    history=StartupHistory(

        user_id=user_id,

        idea=idea,

        ceo=result.get("CEO",""),

        marketing=result.get("Marketing",""),

        sales=result.get("Sales",""),

        hr=result.get("HR",""),

        finance=result.get("Finance","")

    )

    db.session.add(history)

    db.session.commit()

    return jsonify(result),200