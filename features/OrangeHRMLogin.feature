Feature: OrangeHRM Login

  Scenario Outline: Login to OrangeHRM with mulyiple Data
    Given I launch Chrome Browser
    When open Homepage
    And enter username "<username>" and password "<password>"
    And click on submit Button
    Then I Should see the Dashboard Page


    Examples:
       | username | password |
       | admin    | admin123 |
       | deepti   | 12344    |
       | suresh   | 4567     |


