from src.logger.logger import AFLogger
from src.applications.github.test_data import test_data
from src.helpers import helper

logger = AFLogger.get_logger("test_api")


def test_search_for_existing_user(github_api_app):
    existing_user_name = test_data.VALID_USER_NAME
    users = github_api_app.search_user(existing_user_name)

    logger.info(f"Total count is {users['total_count']}")

    assert users["total_count"] != 0


def test_search_for_non_existing_user(github_api_app):
    non_existing_user_name = helper.create_random_data(20)
    users = github_api_app.search_user(non_existing_user_name)

    logger.info(f"Total count is {users['total_count']}")

    assert users["total_count"] == 0


def test_search_for_existing_repo(github_api_app):
    existing_repo_name = test_data.VALID_REPO_NAME
    repos = github_api_app.search_repos(existing_repo_name)

    logger.info(f"Total count is {repos['total_count']}")

    assert repos["total_count"] != 0


def test_search_for_non_existing_repo(github_api_app):
    non_existing_repo_name = helper.create_random_data(20)
    repos = github_api_app.search_repos(non_existing_repo_name)

    logger.info(f"Total count is {repos['total_count']}")

    assert repos["total_count"] == 0


def test_search_for_existing_commit_hash(github_api_app):
    existing_commit_hash = test_data.VALID_COMMIT_HASH
    commit_hashes = github_api_app.search_commits(existing_commit_hash)

    logger.info(f"Total count is {commit_hashes['total_count']}")

    assert commit_hashes["total_count"] != 0


def test_search_for_non_existing_commit_hash(github_api_app):
    non_existing_commit_hash = helper.create_random_data(20)
    commit_hashes = github_api_app.search_commits(non_existing_commit_hash)

    logger.info(f"Total count is {commit_hashes['total_count']}")

    assert commit_hashes["total_count"] == 0
