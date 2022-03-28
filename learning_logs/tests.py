from django.test import TestCase
# Create your tests here.


import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
    import django
    django.setup()
    from learning_logs import models
    models.Topic.objects.all()
