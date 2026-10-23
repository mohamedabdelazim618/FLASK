from flask import Flask
from doctors import doctors_bp
from patients import patients_bp

app = Flask(__name__)


app.register_blueprint(doctors_bp, url_prefix='/doctors')
app.register_blueprint(patients_bp, url_prefix='/patients')


if __name__ == '__main__':
    app.run(debug=True)
