Feature: login finexity

    Scenario Outline: Verify that login should successful using valid creds
        Given refresh browser
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password   |         
            | testuser53@finexity.com | tests!rock |
         
        When User clicks on Login button
        Then user should be logged in
        When User clicks the option to log out by clicking the user icon
        When user click on logout option
        
    Scenario Outline: Check login functionality using invalid user name
        Given refresh browser
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username        | password     |         
            | testuser01@.com | tests!rock   |
        When E-Mail address invalid message should be show 

    Scenario Outline: Check login functionality using invalid password
        Given refresh browser
        Given User is on Finexity website
        When user enters "<username>" and "<password>"
        Examples:
            | username                | password  |         
            | testuser01@finexity.com | INVALID   |
        When User clicks on Login button
        When Wrong email or password. should be show 

    Scenario:Check login functionality using blank email
        Given refresh browser
        Given User is on Finexity website
        Then User provides registration password as "tests!rock" on login page
        When User clicks on Login button
        Then E-Mail address is required should be show 

    Scenario:Check login functionality using blank password
        Given refresh browser
        Given User is on Finexity website
        Then User provides registration email as "testuser14@finexity.com" on login page
        When User clicks on Login button
        Then Password is required should be show 
