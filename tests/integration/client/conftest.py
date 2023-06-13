import pytest

from tests.mocks.client_mocks import DeribitClientMock


@pytest.fixture
def client_mock() -> DeribitClientMock:
    return DeribitClientMock()
