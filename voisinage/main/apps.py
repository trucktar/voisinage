from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'voisinage.main'

    def ready(self):
        from voisinage.main import signals
