Feature: Inverse Matrix
  Scenario: Inverse valid matrix
    Given matrix [[2, 1], [4, 3]]
    When Inversing
    Then result should be [[1.5, -0.5], [-2, 1]]

  Scenario: Inverse singular matix
    Given matrix [[1, 2], [2, 4]]
    When Inversing
    Then result should be None