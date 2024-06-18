from flask import Flask
from controllers.posts_controller import posts_blueprint

app = Flask(__name__)

app.register_blueprint(posts_blueprint)

if __name__ == '__main__':
    app.run(debug=True)