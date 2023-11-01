def test_search_for_existing_user(github_api_client):
    existing_user_name = 'KatarzynaJuszczak'
    users = github_api_client.search_user(existing_user_name)

    print(f"Checking total count is {users['total_count']}")
    assert users['total_count'] != 0


def test_search_for_nonexisting_user(github_api_client):
    nonexisting_user_name = 'sjkfkjhsakjfsdajfsdjfjksdfjddjfdfjkdf'
    users = github_api_client.search_user(nonexisting_user_name)

    print(f"Checking total count is {users['total_count']}")
    assert users['total_count'] == 0


def test_search_for_existing_repo(github_api_client):
    existing_repo_name = 'BecomeQAEngineerCourse'
    repos = github_api_client.search_repos(existing_repo_name)

    print(f"Checking total count is {repos['total_count']}")
    assert repos['total_count'] != 0


def test_search_for_nonexisting_repo(github_api_client):
    nonexisting_repo_name = 'sfbsfbhbjfjsfsdsdjfhsfjadfh'
    repos = github_api_client.search_repos(nonexisting_repo_name)

    print(f"Checking total count is {repos['total_count']}")
    assert repos['total_count'] == 0


def test_search_for_nonexisting_commit_hash(github_api_client):
    nonexisting_commit_hash = 'lnasdklfnkjanskdjfnkjabsdjhfuyagsuygfuyagsduyfgauysdf'
    commit_hashes = github_api_client.search_commits(nonexisting_commit_hash)

    print(f"Checking total count is {commit_hashes['total_count']}")
    assert commit_hashes['total_count'] == 0
