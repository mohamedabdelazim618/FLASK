from flask import Blueprint



patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/')
def list_patients():
    return "Hello patients"