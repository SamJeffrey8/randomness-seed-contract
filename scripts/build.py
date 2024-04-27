import subprocess
from pathlib import Path

from src.on_chain import seed


def main():
    script = Path(seed.__file__).absolute()
    subprocess.run(f"opshin build {script}".split())


if __name__ == "__main__":
    main()
