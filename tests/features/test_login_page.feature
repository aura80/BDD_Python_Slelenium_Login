Feature: login on the nopcommerce website

    Scenario: test login successfully
        Given open the nopcommerce homepage
        When click on register button
        And enter firstname "Anna"
        And enter lastname "Popescu"
        And enter email "abcd@yahoo.com"
        And enter password "Admin123!"
        And confirm passwordconf "Admin123!"
        And register on the page
        And logout
        And click on sign in button
        And enter email "tantamarasescu@yahoo.com"
        And enter password "Admin123!"
        And click on login button
        Then logout from the page