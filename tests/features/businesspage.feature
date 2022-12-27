Feature: Check Business page check 
    Scenario:check Business page
        Given User is on Finexity Homepage 
        When user clicks on business tab of home page
        And Page title is Open Banking Features | FINEXITY Business 
        And Verify top manu content
        And Verify that header is displayed
        
    Scenario: check solution
        Given User is on Finexity Homepage
        When user clicks on business tab of home page 
        When user hoverover on solution option 
        And solution pop should be open 
        
    Scenario: check discover
        Given User is on Finexity Homepage
        When user clicks on business tab of home page 
        When user hoverover on discover option 
        And discover pop should be open 
        
    Scenario: company
        Given User is on Finexity Homepage
        When user clicks on business tab of home page 
        When user hoverover on company option 
        And company pop should be open 
    
    Scenario: Registered user can request information on Open Banking page
        Given User testuser11 is logged in
        Given User is on Finexity Homepage
        When user clicks on logo
        When user clicks on business tab of home page
        And User is on Business page
        When user hoverover on solution option
        And User clicks on Open Banking for Tokenized Assets button
        And User is on Open Banking page
        And User requests information with message Test Message
        Then Verify that message was sent successfully

    Scenario Outline: Registered user can request information on Business pages
    Given User testuser11 is logged in
    Given User is on Finexity Homepage
    When user clicks on logo
    When user clicks on business tab of home page
    When user hoverover on solution option
    And User clicks on <page> menu
    And User requests information with message Test Message
    Then Verify that message was sent successfully
    Examples: Sub Pages
      | page                              |
      | Open Banking for Tokenized Assets |
      | Asset Provider                    |
      | Distributors                      |
      | Investors                         |