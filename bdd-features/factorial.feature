Feature: factorial
  Scenario: Factorial of 0
    Given 0
    When calculating factorial
    Then expect result to be 0
  Scenario: Factorial of positive number
    Given 5
    When calculating factorial
    Then expect result to be 120

  Scenario: Factorial of negative number
    Given -5
    When calculating factorial
    Then expect result to be None
