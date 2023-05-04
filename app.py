from mindspaze_api import appClass


class app:
    def create_app():
        temp = appClass()

        app = temp.create_app()
        return app