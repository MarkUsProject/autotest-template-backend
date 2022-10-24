""" TODO: add a docstring for your backend here """

from typing import Union, List, Dict


def run_test(
    settings_id: Union[int, str],
    test_id: Union[int, str],
    files_url: str,
    categories: List[str],
    user: str,
    test_env_vars: Dict[str, str],
) -> None:
    """
    Run a single test with the files from files_url using the settings with id settings_id that match the category
    in categories.
    test_env_vars are passed to the test as additional anvironment variables.
    user is used to authenticate with the request to the client to retrieve the files at files_url.

    Results from the test are written back to the redis database using the test_id to label the results.
    """
    # TODO: write the code that runs tests here
    #       Test results should be written to the autotest:test_result:X (where X == test_id) in the redis database.
    #       The content of each feedback file should be written to autotest:feedback_file:X:Y (where X == test_id and
    #       Y is a unique id for that specific feedback file).
    #       Test results must respect the schema in result_schema.json


def update_test_settings(user: str, settings_id: Union[str, int], test_settings: Dict, file_url: str) -> None:
    """
    Update the test settings with id == settings_id to test_settings.
    user is used to authenticate with the request to the client to retrieve the files at files_url.

    Updated settings will be written back to the redis database, files downloaded from file_url will
    be stored on disk with files used to create the test environment (for example, a python virtual
    environment or directory of R packages).
    """
    # TODO: write the code that updates test settings here. Updated settings should be written to the autotest:settings
    #       hash in the redis database where the hash key is settings_id and the value is the updated settings.
