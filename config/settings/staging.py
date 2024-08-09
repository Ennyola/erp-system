import os

import dj_database_url

from .base import *

DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
