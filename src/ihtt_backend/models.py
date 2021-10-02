import databases
import orm
import pendulum
import platformdirs

data_path = platformdirs.user_data_path() / "ihtt"
if not data_path.exists():
    data_path.mkdir(parents=True)

database = databases.Database(f"sqlite:///{data_path.as_posix()}/db.sqlite")
models = orm.ModelRegistry(database=database)


class Session(orm.Model):
    registry = models
    fields = {
        "id": orm.UUID(primary_key=True),
        "description": orm.Text(),
        "start": orm.DateTime(allow_null=True),
        "end": orm.DateTime(allow_null=True),
        # tags?
    }


class Reporter(orm.Model):
    registry = models
    fields = {
        "id": orm.UUID(primary_key=True),
        "slug": orm.String(max_length=100, index=True),
        "description": orm.Text(),
    }


class Entry(orm.Model):
    registry = models
    fields = {
        "id": orm.UUID(primary_key=True),
        "description": orm.Text(),
        "timestamp": orm.DateTime(default=pendulum.now, index=True),
        "session": orm.ForeignKey(Session, allow_null=True),
        "reporter": orm.ForeignKey(Reporter, allow_null=True),
        # tags?
    }


models.create_all()
