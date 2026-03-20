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


def format_fixture(given, when, then):
    return f"GIVEN:\n{given}\n\nWHEN:\n{when}\n\nTHEN:\n{then}\n"


def test_show_empty():
    output = run_dt("show").strip()
    result = format_fixture(".", "dt show", output)
    verify(result)
