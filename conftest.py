from django.test.utils import setup_test_environment
from django.conf import settings


def pytest_configure(config) -> None:
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
