from pathlib import Path
from portalbrasil.core.interfaces import IBrowserLayer
from portalbrasil.core.utils.scripts import create_site

import os


SCRIPT_DIR = Path().cwd() / "scripts"

ANSWERS = {
    "site_id": os.getenv("SITE_ID"),
    "title": os.getenv("SITE_TITLE"),
    "description": os.getenv("SITE_DESCRIPTION"),
    "distribution": os.getenv("DISTRIBUTION"),
    "default_language": os.getenv("SITE_DEFAULT_LANGUAGE"),
    "portal_timezone": os.getenv("SITE_PORTAL_TIMEZONE"),
    "setup_content": os.getenv("SITE_SETUP_CONTENT", "true"),
}


def main():
    app = globals()["app"]
    filename = os.getenv("ANSWERS", "default.json")
    answers_file = SCRIPT_DIR / filename
    create_site(app, ANSWERS, answers_file, IBrowserLayer)


if __name__ == "__main__":
    main()
