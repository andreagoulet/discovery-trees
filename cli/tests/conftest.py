import pytest
from approvaltests import set_default_reporter
from approvaltests.reporters import PythonNativeReporter


@pytest.fixture(scope="session", autouse=True)
def configure_approvaltests():
    set_default_reporter(PythonNativeReporter())
