from behave import given, when, then
from main import matrix_sum
import numpy as np


@given("{matrix1} and {matrix2}")
def step_given_two_matrix(context, matrix1, matrix2):
    context.matrix1 = eval(matrix1)
    context.matrix2 = eval(matrix2)


@when("summing")
def step_summing_matrix(context):
    context.result = matrix_sum(context.matrix1, context.matrix2)
    print(context.matrix1, context.matrix2, context.result)


@then("expect result to be {expected_result}")
def step_then_verify_result(context, expected_result):
    assert np.array_equal(eval(expected_result), context.result)

