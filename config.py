import os
import secrets

CONFIGURATION = {
    "NAME": "PROJECT_NAME",  # Name of the Service
    "DEBUG": True,
    "ALLOWED_HOSTS": ["*"],
    "SERVICE_SECRET_KEY": os.environ.get(
        "SERVICE_SECRET_KEY", secrets.token_hex(25)
    ),  # Service secret key
    "INSTALLED_APPS": ["core"],
    # Database config if using MySQL
    "DATABASE": {
        "name": os.environ.get("DB_NAME", "DB_NAME"),
        "user": os.environ.get("DB_USERNAME", "root"),
        "password": os.environ.get("DB_PASSWORD", "root"),
        "options": {"host": "localhost", "port": "3306", "dialect": "mysql"},
    },
    "datetime_format": "%Y-%m-%d %H:%M:%S",
    "cache": {"ttl": {"sec": 86400}},
    "crons": {
        # Appname : Crons list
        "core": [
            {
                "name": "CronName",
                "enabled": False,
                "frequency": "30 1 * * *",
                "handler": "core.crons.cronhandler.main",
                "args": [{}],
            }
        ]
    },
}
