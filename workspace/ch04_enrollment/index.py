from flask import Flask
from controller.enrollment_controller import enrollment_blueprint

app = Flask(__name__)

app.register_blueprint(enrollment_blueprint)

if __name__ == '__main__':
    app.run(port=5001)


