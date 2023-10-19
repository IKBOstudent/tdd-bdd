from behave import given, when, then
from main import get_inverse_matrix
import numpy as np


@given("matrix {matrix}")
def step_given_matrix(context, matrix):
    context.matrix = eval(matrix)


@when("inversing")
def step_summing_matrix(context):
    context.result = get_inverse_matrix(context.matrix)


@then("result should be {expected_result}")
def step_then_verify_result(context, expected_result):
    assert np.array_equal(eval(expected_result), context.result)

