Feature: Adequacy process
    Scenario: User can cancel an ongoing adequacy process
        Given User testuser07 is logged in
        When User opens Account sidebar
        And User clicks on adequacy check button
        when User clicks on Continue button for adequacy
        And User selects Asset Manager option
        when User clicks on Continue button
        And User clicks on Cancel Adequacy Check button
        Then Verify that I would like to provide information button is displayed on sidebar

    Scenario: User can complete adequacy check without an exam
        Given User testuser07 is logged in
        When User opens Account sidebar
        And User clicks on adequacy check button
        And User clicks on I do not want to provide any information button
        And User clicks on I want to continue without an exam button
        Then Success message is displayed
        And User clicks on Exit button
        And Verify that user is redirected to dashboard page
        And User waits for 10 sec
        And Verify that adequacy tile is not displayed on dashboard

