import subprocess


def run_dt(*args):
    result = subprocess.run(
        ["dt", *args],
        capture_output=True,
        text=True,
        cwd=None,
    )
    return result.stdout


