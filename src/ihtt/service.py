from fastapi import FastAPI
from .models import Entry
from .schemas import PydEntry

app = FastAPI(title="I Hate Time Tracking")


@app.post("/entries", response_model=PydEntry)
async def create_entry(entry: PydEntry):
    entry_obj = await Entry.create(**entry.dict(exclude_unset=True))
    return await PydEntry.from_tortoise_orm(entry_obj)
