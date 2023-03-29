# Bank/ATM Django REST API 
<p>Jennifer Kaiser 2023 
<p>
<a href="https://www.jenniferkaiser.tech">www.jenniferkaiser.tech</a>
<p>
<a href="https://www.linkedin.com/in/jenniferkaiser-tech">www.linkedin.com/in/jenniferkaiser-tech</a>
<p>
<a href="https://www.github.com/jenniferkaiser21">www.github.com/jenniferkaiser21</a>

# Demo of Working Code
<a href="#">Link coming soon!</a>


# Languages Used:
* Python (Version 3.9.12)

# Packages/Libraries Used:
* Django
* djangorestframework

# IDE Used:
* VSCode

# Version Control:
* Git

# Summary of Project:
https://github.com/jenniferKaiser21/Bank

This project is a work in progress, and simulates the tasks that a traditional bank or ATM might need to process on a daily basis, including account creation and establishing a balance, and executing common banking transactions such as withdrawals and deposits, while tabulating the resulting balance and logging all transaction data including starting and ending balances and transaction timestamp.

In order to build this simulation, the Django Rest Framework is used to build the back-end API, so that various endpoints can take GET/POST requests with payload data for simulation.

# Current endpoints:
myaccount/ (GET REQUEST)

<img src="https://github.com/jenniferKaiser21/Bank/blob/81df1ed2984fbbbf786b02b55b0f080e0ce5a381/images/myaccount_get.png">

newaccount/ (POST REQUEST)

<img src="https://github.com/jenniferKaiser21/Bank/blob/81df1ed2984fbbbf786b02b55b0f080e0ce5a381/images/newaccount_endpoint.png">

transaction/\<int:id\> (GET REQUEST)

<img src="https://github.com/jenniferKaiser21/Bank/blob/81df1ed2984fbbbf786b02b55b0f080e0ce5a381/images/transaction_endpoint_url_id.png">

newtransaction/ (POST REQUEST)

<img src="https://github.com/jenniferKaiser21/Bank/blob/595419e08c1bffdfbe1cbc35790d8b1dd9db718d/images/newtransaction_post_request.png">


# Database Models
The Accounts database table contains the following attributes:

    first_name (a character field)
    last_name (a character field)
    date_opened (a date field that is automatated using the auto_now_add = True clause)
    last_updated (a date field that is automatated using the auto_now = True clause)
    balance (a decimal field with a maximum of 20 digits and 2 decimal places)
    pin (a numeric code stored as a string with a length of 4)

The Transactions database table contains the following attributes:

    timestamp (a date field that is automatated using the auto_now_add = True clause)
    account_id (a foreign key mapped to the Accounts.id primary key of the Accounts table)
    transaction_amt (a decimal field with a maximum of 20 digits and 2 decimal places)
    transaction_type (a choice field referring to transaction type codes such as "WD" "withdrawal" and "DP" for deposit)
    starting_balance (a decimal field with a maximum of 20 digits and 2 decimal places)
    ending_balance (a decimal field with a maximum of 20 digits and 2 decimal places)

# Additional Notes:

