Feature: Finexity Homepage
    Background:check personal tab
        Given User is on Finexity website
        When user clicks on logo
        And Verify top menu content
        And Verify that header is displayed
        And Verify that footer is displayed 
        When user click on personal tab
        
    Scenario:check personal tab
        when user click on join now botton on personal tab
        when user clicks on register now botton on personal tab
        And user check that footer links 

    Scenario: check marketplace on personal page
        when user click on marketplace tab
        And user check marketplace cetagory tab 
        When user clicks on marketplace cetagory tab
        And user check marketplace product
        When user clicks on marketplace product details

    Scenario: check digital wealth of home page  
        When hoverover on digital wealth tab 
        when user click on digital wealth items
    
    Scenario: check company of home page 
        When hoverover on company tab 
        when user click on company items
   
    








    

    




        