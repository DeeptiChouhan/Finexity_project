Feature: InvestmentPage from finexity
    Scenario: investment flow
        Given User testuser53 is logged in
        When user click on marketplace tab
        When user select 'Green Tiny House Jan' property from Investments tab
        When user click on Invest now button
        When user enter amount 
        when User clicks on Continue button
        Then user clicks on start button 
        when User clicks on Continue button
        when User clicks on Continue button
        When user select payment method
        then user clicks on Costs and grants
        then User checks all tick boxes
        then clicks on buy now on Overview page
        then user click on back to production page 
        And User navigates to dashboard page
        Then Investment status is updated to Investment started on user dashboard
        And Verify data in investment tile on user dashboard
            | FIELD                    | VALUE |
            | Number of digital shares | 800   |
        
    Scenario: User can abort an existing investment
        Given User testuser53 is logged in
        When user click on marketplace tab
        When user select 'Biondi-Santi Riserva (2015)' property from Investments tab
        When user click on Invest now button
        When user enter amount 
        when User clicks on Continue button
        Then user clicks on start button
        And User closes investment sidebar
        When user click on Invest now button
        Then User closes investment sidebar
        And User navigates to dashboard page
        And refresh browser
        Then Aborted investment is not displayed on user dashboard


    Scenario: user can download document
        Given User testuser53 is logged in
        When user click on marketplace tab
        When user select 'Green Tiny House Jan' property from Investments tab
        When user click on Invest now button
        When user enter amount 
        when User clicks on Continue button
        Then user clicks on start button 
        when User clicks on Continue button
        when User clicks on Continue button
        When user select payment method
        then user clicks on Costs and grants
        then User should be download that document