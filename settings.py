INSTALLED_APPS = [
    "django_rq",
]

# Django-RQ Configuration
RQ_QUEUES = {
    "default": {"HOST": "localhost", "PORT": 6379, "DB": 0, "DEFAULT_TIMEOUT": 360,},
}