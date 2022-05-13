from pytest_bdd import (given, scenario, when, then, parsers)
from staf_util.globalutils.api_hooks import Hooks
from api.logic.process_api_requests import ApiTesting
from ui.ui_automation_functions import UiTesting

obj_hook = Hooks()
obj_api_Testing = ApiTesting()
obj_ui_testing = UiTesting()


@scenario('api_scenarios/api_usres_rest_api.feature', 'api_sample_scenario_api')
def test_api_scenario():
    """testing_api_scenario"""


@scenario('api_scenarios/api_usres_rest_api.feature', 'ui_based_test_scenarios_ui')
def test_ui_scenario():
    """testing_api_scenario"""


@when(obj_hook.data_table('user hit the following url to perform get operation', str_fixture='data'))
def user_hit_endpoint(data):
    for row in data:
        url = row["url"]
        assert obj_api_Testing.api_call(str_url=url)


@then('user should get an OK response')
def check_ok_response():
    assert obj_api_Testing.very_response_code()


@then(obj_hook.data_table('I should see the following information', str_fixture='data'))
def verfiy_information(data):
    for row in data:
        keyword = row["keyword"]
        assert obj_api_Testing.verify_data(str_keyword=keyword)


@when(obj_hook.data_table('user hit the following url to load in the ui', str_fixture='data'))
def user_navigate_to_url(data):
    for row in data:
        url = row["url"]
        assert obj_ui_testing.navigateto(url)


@then(obj_hook.data_table('user should see the following keywords on the page', str_fixture='data'))
def verfiy_information_on_the_ui_page(data):
    for row in data:
        str_keyword = row["keyword"]
        assert obj_ui_testing.verify_string(keyword=str_keyword)


@then('close the browser')
def close_browser():
    obj_ui_testing.close_driver()
