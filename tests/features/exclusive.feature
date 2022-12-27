Feature: Finexity Exclusive page 
    Background: Check full Exclusive page
        Given User is on Finexity Homepage
        When user clicks on exclusive tab
        And Verify top menu content 
        And Verify header of exclusive

    Scenario: check marketplace of exclusive page
        Given exclusive page should be open 
        When clicks on marketplace tab
        And marketplace page open with product 

    Scenario: check digital wealth of exclusive page
        Given exclusive page should be open
        When user clicks on exclusive tab 
        When hoverover on digital wealth tab 
        when user click on digital wealth items
    
    Scenario: check company of exclusive page
        Given exclusive page should be open 
        When hoverover on company tab 
        when user click on company items
  
      


     
