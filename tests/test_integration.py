import requests
from dotenv import load_dotenv, find_dotenv
import pytest
import app


@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client


class MockResponse:
    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        x = [
                {"id": "1", "idList": "5ef48eae04ceb72b492830ef", "name": "ItemInTodo", "dateLastActivity": "2020-07-24T08:05:34.790Z"},
                {"id": "2", "idList": "5f117c1d6bd68417cc8566c1", "name": "ItemInProgress", "dateLastActivity": "2020-07-24T08:05:34.790Z"},
                {"id": "3", "idList": "5ef48eb03da6260d87a4e9ab", "name": "ItemCompleted", "dateLastActivity": "2020-07-24T08:05:34.790Z"},
                {"id": "4", "idList": "5ef48eb03da6260d87a4e9ab", "name": "AncientItemCompleted", "dateLastActivity": "2020-06-24T08:05:34.790Z"}
            ]
        return x


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)


def test_index_page(mock_response, client):
    response = client.get('/')
    assert 'ItemInTodo' in str(response.data)
    assert 'ItemInProgress' in str(response.data)
    assert 'ItemCompleted' in str(response.data)
    assert 'AncientItemCompleted' in str(response.data)

