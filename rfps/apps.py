from django.apps import AppConfig


class RfpsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rfps'

    def ready(self):
        import rfps.signals