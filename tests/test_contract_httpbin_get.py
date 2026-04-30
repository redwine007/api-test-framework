import http_client
from jsonschema import validate


def test_httpbin_get_json_matches_minimal_schema(base_url, timeout_seconds):
    url = f"{base_url}/get"
    resp = http_client.http_get(url, timeout=timeout_seconds, token="")

    assert resp.status_code == 200

    data = resp.json()

    # JSON Schema
    # required：顶层必须存在的字段
    # type：字段类型约束
    schema = {
        "type": "object",
        "required": ["args", "headers", "url"],
        "properties": {
            "args": {"type": "object"},
            "headers": {"type": "object"},
            "url": {"type": "string"},
        },
    }

    # validate：不符合 schema 会抛 JSONSchemaError（pytest 会标记失败）
    validate(instance=data, schema=schema)