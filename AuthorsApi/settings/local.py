from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default='ctCGZD41NwBLsjoJ-SjuYFv6xXxm3l6PBTSB7EE1X-UAzqb2FV4')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]