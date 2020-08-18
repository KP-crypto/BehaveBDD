Feature: OrangeHRM Logo

  Scenario: Logo present on Orange site
    Given launch Chrome Browser
    When  User is on HomePage
    Then OrangeHRM logo should be present
    And Close Browser