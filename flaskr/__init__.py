import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def hello_world():
        return 'Hello,World!'

    @app.route('/name', methods=['GET', 'POST'])
    def get_name():
        if request.method == 'POST':
            return 'merlinalex from POST'
        else:
            return 'merlinalex from GET'

    @app.route('/fans')
    def get_fans():
        return '100000'

    ## 用户资料
    @app.route('/userProfile', methods=["GET", "POST"])
    def get_profile():
        if request.method == 'GET':
            name = request.args.get('name', '')
            print(name)
            if (name == 'merlinalex'):
                return dict(name='merlinalex from GET', fans=100000)
            else:
                return dict(name='not merlinalex', fans=10000000)
        elif request.method == 'POST':
            print(request.form)
            print(request.data)
            print(request.json)
            name = request.json.get('name')
            if (name == 'merlinalex'):
                return dict(name='merlinalex from POST', fans=100000)
            else:
                return dict(name='not merlinalex from POST', fans=10000000)
            return '1'

    return app