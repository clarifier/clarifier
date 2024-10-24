import clickhouse_connect
from django.conf import settings


def clickhouse():
    _settings = settings.CLICKHOUSE
    return clickhouse_connect.get_client(
        host=_settings.get("host"),
        username=_settings.get("username"),
        password=_settings.get("password"),
    )


__all__ = ["clickhouse"]
