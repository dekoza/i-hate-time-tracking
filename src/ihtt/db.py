import platformdirs
from aerich import Command

_DATA_PATH = platformdirs.user_data_path() / "ihtt"
DB_PATH = _DATA_PATH / "db.sqlite"

TORTOISE_CONFIG = {
    "connections": {
        "default": f"sqlite://{DB_PATH.as_posix()}",
    },
    "apps": {
        "models": {"models": ["ihtt.models", "aerich.models"]},
    },
}


async def init_db():
    if not _DATA_PATH.exists():
        _DATA_PATH.mkdir(parents=True)

    command = Command(tortoise_config=TORTOISE_CONFIG, app="models")
    await command.init()
    await command.migrate("ihtt")

    # schemas need to be initialized after Tortoise
    from .schemas import PydReporter, PydSession, PydEntry  # noqa
