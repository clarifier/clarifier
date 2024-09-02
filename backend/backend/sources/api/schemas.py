from typing import Optional
from ninja import ModelSchema, Schema
from sources.models import Source


class SourceSchema(ModelSchema):
    class Meta:
        model = Source
        fields = "__all__"


class UploadSource(Schema):
    name: str
    description: str


class SourceFromFile(UploadSource):
    pass


class SourceFromURL(UploadSource):
    url: str


class SourceFromOpenML(Schema):
    openml_id: str


class SourceFromTFDS(Schema):
    tfds_id: str


class SourceFromPostgreSQL(Schema):
    hostname: str
    username: str
    password: str
    ssl: bool
    table: Optional[str]
    check: bool
