Feature: Matrix Sum
  Scenario: Sum empty matrix
    Given [[]] and [[]]
    When summing
    Then expect result to be [[]]

  Scenario: Sum matrix with different dimensions
    Given [[1, 2, 3], [4, 5, 6]] and [[7, 8], [10, 11]]
    When summing
    Then expect result to be None

  Scenario: Sum matrix of same dimensions
    Given [[1, 2, 3], [4, 5, 6]] and [[7, 8, 9], [10, 11, 12]]
    When summing
    Then expect result to be [[8, 10, 12], [14, 16, 18]]

