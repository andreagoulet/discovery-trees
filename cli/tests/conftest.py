import pytest
from approvaltests import set_default_reporter
from approvaltests.reporters import (
    GenericDiffReporter,
    GenericDiffReporterConfig,
    MultiReporter,
    PythonNativeReporter,
)


def _vscode_reporter():
    config = GenericDiffReporterConfig("VS Code", "/opt/homebrew/bin/code", ["--diff"])
    return GenericDiffReporter(config)


@pytest.fixture(scope="session", autouse=True)
def configure_approvaltests():
    set_default_reporter(MultiReporter(PythonNativeReporter(), _vscode_reporter()))
