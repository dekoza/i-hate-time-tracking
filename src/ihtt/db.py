import platformdirs
from tortoise import Tortoise


async def init_db():
    data_path = platformdirs.user_data_path() / "ihtt"
    db_path = data_path / "db.sqlite"
    if not data_path.exists():
        data_path.mkdir(parents=True)
    if not db_path.exists():
        await Tortoise.init(
            db_url=f"sqlite://{db_path.as_posix()}",
            modules={"models": ["ihtt.models"]},
        )
        await Tortoise.generate_schemas()
