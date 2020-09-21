from django.apps import AppConfig


class FffConfig(AppConfig):
    name = 'fff'

    def ready(self):
        import fff.signals
