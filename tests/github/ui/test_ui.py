from src.logger.logger import AFLogger

logger = AFLogger.get_logger("test_ui")


def test_github_login_negative_page_obj(github_login_page_object):
    github_login_page_object.try_to_login("wrong username", "wrong password")

    error_message_text = github_login_page_object.check_error_message().text
    logger.debug(f"Error message: {error_message_text}")

    assert error_message_text == "Incorrect username or password."
