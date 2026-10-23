
from flask import Blueprint


doctors_bp = Blueprint('doctors', __name__)

@doctors_bp.route('/')
def list_doctors():
    return "Hello doctors"
