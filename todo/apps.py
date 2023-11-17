from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'  # Change 'myapp' to the actual name of your app

    def ready(self):
        import todo.signals 