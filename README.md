# CloudFlare Audit

### A tool to query each CloudFlare domain in multiple organisations and send an aggregated email of their zone records. 

#### What do you need?
* SMTP Server / Account (SSL)
* CloudFlare API Token with Read Privileges 

#### What do you get?
1. A CSV file is created for each zone in the account.
2. An aggregated email with all records in all zones.

#### References  
* https://realpython.com/python-send-email/
* https://api.cloudflare.com/
