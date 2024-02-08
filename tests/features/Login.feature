Feature: Login
  In order to maintain patient records
  As a user
  I want to access OpenEMR portal


  Scenario Outline: Valid Login
    Given I have browser with OpenEMR application
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I click on login
    Then I should get access to portal with title "<expected_title>"
    Examples:
      | username     | password     | expected_title |
      | admin        | pass         | OpenEMR        |
      | receptionist | receptionist | OpenEMR        |

  Scenario: Invalid Login
    Given I have browser with OpenEMR application
    When I enter username as "john"
    And I enter password as "john123"
    And I click on login
    Then I should not get access to portal with error "Invalid username or password"

