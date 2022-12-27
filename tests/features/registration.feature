Feature: User Registration
    Scenario:New user can be registered using email 
      When User clicks on registration link
      And User is on registration page   
      when User provides registration email as "testuser14@finexity.com" on registration page
      when User clicks on Create Account button
      when User clicks on Continue button
      when User provides registration password as "tests!rock" on registration page
      when User clicks on Continue button
      Then Verify that new user registration was successful
      when User clicks on Exit Registration button

    Scenario Outline: After registration user onboarding
      When user enters "<username>" and "<password>" for registration
        Examples:
            | username                | password   |         
            | testuser14@finexity.com | tests!rock |
      When User clicks on Login button
      Then Verify that user is redirected to User-onboarding page
      when User clicks on Continue button
      When User clicks on Skip button on complete your personal data page
      When User clicks on Skip button on Your Interests
      When User enters mobile number as "45645678"
      When User clicks on Request code button with wait of 5 sec
      When User enters TAN as 999999
      And User waits for 10 sec
      when User clicks on Continue button 
      When User checks all tick boxes
      And User clicks on Continue button on Conditions page
      And User waits for 10 sec
      And User clicks on To Dashboard button on Congratulations page
      And Verify that user is redirected to Dashboard page
    

    Scenario:New user can be registered using mobile
      When User clicks on registration link
      And User is on registration page
      when User provides registration mobile_number as "999999"
      when User clicks on Create Account button
      when User clicks on Continue button
      when User provides registration email as "testuser14@finexity.com" on registration page
      when User provides registration password as "tests!rock"
      when User clicks on Continue button
      Then Verify that new user registration was successful
      when User clicks on Exit Registration button
      

    Scenario Outline: Password length should be Minimum 6
      When User clicks on registration link
      And User is on registration page
      when User provides registration email as "testuser14@finexity.com" on registration page
      when User clicks on Create Account button
      when User clicks on Continue button
      when User provides registration password as "<password>" 
      when User clicks on Continue button with 1 error handled
      Then Verify error message "<message>"
          Examples:
            | password | message                                     |         
            | tests    | Minimum password length should be 6 symbols |

    Scenario:  Password is requirements for user registration
      Given User is on Finexity Homepage
      When User clicks on registration link
      And User is on registration page
      when User provides registration email as "testuser14@finexity.com" on registration page
      when User clicks on Create Account button
      when User clicks on Continue button
      when User tries to register without entering the password then
      Then Verify blank password error message "Password is required"
      

    Scenario: user should be register with valid Email address
      Given User is on Finexity Homepage
      When User clicks on registration link
      And User is on registration page
      And User provides registration email as "<email>" on registration page
      when User clicks on Create Account button
      Then Verify invalid error message "E-Mail address invalid"
    

    Scenario Outline: User should be register with valid Mobile Number
      When User clicks on registration link
      And User is on registration page
      And User provides registration mobile_number as "<mobile_number>"
      when User clicks on Create Account button
      Then Verify error message <message>
      Examples: Password Check
        | mobile_number | message               |
        | 9999          | Invalid mobile number |

    Scenario:Verify user can not Signup with existing Email address and gets message
      When User clicks on registration link
      And User is on registration page
      When User provides registration email as "deepti.chouhan+05@encoresky.com" on registration page
      When User clicks on Create Account button
      Then User verifies The Email address cannot be used for registration. Check if you already have a FINEXITY account. is displayed


    


      