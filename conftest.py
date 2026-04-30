import pytest
import config


@pytest.fixture
def base_url():
    return config.get_base_url()


@pytest.fixture
def timeout_seconds():
    return config.get_timeout_seconds()


@pytest.fixture
def test_context():
    print("\n[SETUP] prepare test context")
    ctx = {"trace_id": "demo-trace", "owner": "qa-learner"}
    yield ctx
    print("[TEARDOWN] cleanup test context")


@pytest.fixture
def bearer_token():
    return config.get_bearer_token()
