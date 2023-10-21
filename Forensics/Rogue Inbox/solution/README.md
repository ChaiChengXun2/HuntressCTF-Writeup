# Rogue Inbox - Forensics Challenge

## Challenge Overview
**Name:** Rogue Inbox  
**Category:** Forensics  
**Points:** 50

## Objective

The objective of the "Rogue Inbox" challenge is to investigate a CSV file that contains data in JSON format. You need to explore the activities recorded in the CSV and identify a particular operation that reveals the flag.

## Solution Steps

To solve this challenge, follow these steps:

1. **Examine the CSV File:**
   - Begin by opening and examining the provided CSV file.
   - The data within this file is stored in JSON format, so it's essential to analyze its contents.

2. **Choose a Viewing Tool:**
   - Although the data can be viewed in Excel, I prefer command line for better searching and filtering capabilities.
   - Use the command line or a tool of your choice to interact with the CSV data.

3. **Identify Operations:**
   - The next step is to identify and understand the different operations recorded in the CSV.
   - Common operations mentioned include:
     - Add service principal
     - Enable-AddressListPaging
     - Set-TransportConfig
     - AppAccessContext
     - Install-AdminAuditLogConfig
     - Set-Mailbox
     - Reset user password
     - Update StsRefreshTokenValidFrom Timestamp
     - UserLoggedIn
     - FileAccessed
     - New-InboxRule
     - and more.

4. **Focus on "New-InboxRule" Operation:**
   - While reviewing the list of operations, I initially suspected that the flag might be related to user passwords because of operations like "user logged in" and "reset user password."
   - However, upon closer examination, it was evident that these operations did not contain the flag.
   - Focus on the "New-InboxRule" operation, as this is where the flag is concealed.
![Flag Hidden Within New Inbox Rule](<new inbox rule.png>)

5. **Extract the Flag:**
   - Use Python or a scripting language of your choice to extract and filter all data associated with the "New-InboxRule" operation.
   - The flag is hidden within this operation; your script should reveal it.
```python
flag = ""

with open("purview.csv", "r") as file:
	content = file.readlines() 

	for line in content:
		if "new-inboxrule" in line.lower():
			flag += line.split(",")[18][-3]

print(flag)
```

**Challenge Solved**

Flag: flag{XXXXXXXXXX}
