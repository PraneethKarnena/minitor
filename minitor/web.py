from threading import Thread

from flask import Flask

from minitor.main import main


def create_app():
    app = Flask(__name__)

    @app.route('/healthcheck')
    def healthcheck():
        return 'OK'

    return app


def start_main_thread():
    thread = Thread(target=main)
    thread.daemon = True
    thread.start()


if __name__ == '__main__':
    start_main_thread()
    create_app().run()
