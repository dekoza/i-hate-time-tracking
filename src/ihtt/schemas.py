from tortoise.contrib.pydantic import pydantic_model_creator

from ihtt.models import Session, Reporter, Entry

PydSession = pydantic_model_creator(Session)
PydReporter = pydantic_model_creator(Reporter)
PydEntry = pydantic_model_creator(Entry)
