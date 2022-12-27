Feature: Check all the public page 
    Scenario: check personal pages
        Given When User visit on finexity website
        When user clicks on personal tab
        And open personal page
        And clicks on register now 

    Scenario Outline: check footer links of personal page on home page 
        Given When User visit on finexity website
        When user clicks on personal tab
        And open personal page
        And clicks on register now
        When clicks one by one on footer "<Links>"
        Examples: check links
            | Links              |
            | Marketplace        |
            | Partner program    |
            | SaaS platform      |
            | Ambassador program |
            | Discover           |
            | Blog               |
            | Knowledge Base     |
            | FAQ                |
            | Glossary           |
            | Company            |
            | About us           |
            | Our team           |
            | We are hiring!     |
            | Press              |
            | Contact            |





