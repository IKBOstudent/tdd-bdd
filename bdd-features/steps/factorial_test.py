from behave import given, when, then
from main import calculate_factorial


@given("{num}")
def step_given_factorial(context, num):
    context.num = eval(num)


@when("calculating")
def step_calculating_factorial(context):
    context.result = calculate_factorial(context.num)


@then("expect result to be {expected_result}")
def step_then_verify_result(context, expected_result):
    assert eval(expected_result) == context.result
