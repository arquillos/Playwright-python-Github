"""Checks for the creation of Issues in Github"""
from playwright.sync_api import APIRequestContext, Page

from config.env import GITHUB_REPO, GITHUB_USER


def test_create_issue(api_context: APIRequestContext):
    """Test the creation of an Issue in the temporary repository"""
    issue_data = {
        "title": "[Bug] This is an issue for a bug",
        "body": "The steps to reproduce the bug are:..."
    }

    response = api_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues",
        data=issue_data
    )
    assert response.ok, "The Issue has not been created!"


def test_take_issues_screenshot(page: Page):
    """This is not a test. Just browsing to the page and taking an screenshot"""
    page.goto(url=f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/issues")
    page.screenshot(path="github_issues.png")


def test_issue_is_in_repo(api_context: APIRequestContext):
    """Check the new issue is created in the repository"""
    all_issues = api_context.get(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues"
    )
    assert all_issues.ok, "There is no issue in the repository"

    new_issue = [
        issue
        for issue in all_issues.json()
    ][0]

    assert new_issue["title"] == "[Bug] This is an issue for a bug"
    assert new_issue["body"] == "The steps to reproduce the bug are:..."
