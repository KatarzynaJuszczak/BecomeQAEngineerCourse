from src.applications.github.api.github_api import TestApiLogger, config


def test_search_for_existing_user(github_api_app):
    TestApiLogger.info("------- test_search_for_existing_user -------")

    existing_user_name = config.VALID_DATA["USER_NAME"]
    users = github_api_app.search_user(existing_user_name)

    TestApiLogger.info(f"Total count is {users['total_count']}")

    assert users["total_count"] != 0


def test_search_for_non_existing_user(github_api_app):
    TestApiLogger.info("------- test_search_for_non_existing_user -------")

    non_existing_user_name = config.NON_VALID_DATA["USER_NAME"]
    users = github_api_app.search_user(non_existing_user_name)

    TestApiLogger.info(f"Total count is {users['total_count']}")

    assert users["total_count"] == 0


def test_search_for_existing_repo(github_api_app):
    TestApiLogger.info("------- test_search_for_existing_repo -------")

    existing_repo_name = config.VALID_DATA["REPO_NAME"]
    repos = github_api_app.search_repos(existing_repo_name)

    TestApiLogger.info(f"Total count is {repos['total_count']}")

    assert repos["total_count"] != 0


def test_search_for_non_existing_repo(github_api_app):
    TestApiLogger.info("------- test_search_for_non_existing_repo -------")

    non_existing_repo_name = config.NON_VALID_DATA["REPO_NAME"]
    repos = github_api_app.search_repos(non_existing_repo_name)

    TestApiLogger.info(f"Total count is {repos['total_count']}")

    assert repos["total_count"] == 0


def test_search_for_existing_commit_hash(github_api_app):
    TestApiLogger.info("------- test_search_for_existing_commit_hash -------")

    existing_commit_hash = config.VALID_DATA["COMMIT_HASH"]
    commit_hashes = github_api_app.search_commits(existing_commit_hash)

    TestApiLogger.info(f"Total count is {commit_hashes['total_count']}")

    assert commit_hashes["total_count"] != 0


def test_search_for_non_existing_commit_hash(github_api_app):
    TestApiLogger.info("------- test_search_for_non_existing_commit_hash -------")

    non_existing_commit_hash = config.NON_VALID_DATA["COMMIT_HASH"]
    commit_hashes = github_api_app.search_commits(non_existing_commit_hash)

    TestApiLogger.info(f"Total count is {commit_hashes['total_count']}")

    assert commit_hashes["total_count"] == 0
