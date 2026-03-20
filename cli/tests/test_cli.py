import subprocess

from approvaltests import verify


def run_dt(*args):
    result = subprocess.run(
        ["dt", *args],
        capture_output=True,
        text=True,
        cwd=None,
    )
    return result.stdout


def test_cli_runs():
    output = run_dt()
    verify(output)
