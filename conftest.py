# from django.test.utils import setup_test_environment
from django.conf import settings
import pytest


def pytest_configure(config: pytest.Config) -> None:
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
