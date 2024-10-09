"""Fixtures"""
import pytest

from playwright.sync_api import Playwright, APIRequestContext

from config.env import GITHUB_ACCESS_TOKEN, GITHUB_REPO, GITHUB_URL, GITHUB_USER


@pytest.fixture(scope="session", name="api_context")
def fixture_api_context(playwright: Playwright) -> APIRequestContext:
    """Setup the API context for Github"""
    context: APIRequestContext = playwright.request.new_context(
        base_url=GITHUB_URL,
        extra_http_headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {GITHUB_ACCESS_TOKEN}"
        }
    )

    yield context

    context.dispose()


@pytest.fixture(autouse=True, scope="session")
def create_test_repository(api_context: APIRequestContext):
    """Create a Github temporary repository and delete it after the tests"""
    # Create the repository
    response = api_context.post(
        "/user/repos",
        data={
            "name": GITHUB_REPO
        }
    )
    assert response.ok, f"The repository {GITHUB_REPO} has not been created!"

    yield

    # Delete the repository
    response = api_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}",
    )
    assert response.ok, f"The repository {GITHUB_REPO} has not been deleted!"
