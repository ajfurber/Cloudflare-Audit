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

#### Known Bugs
1. [Limit of 100 Records per Zone](https://git.aylo.net/noauth/cloudflare-audit/-/issues/1)


This tool is updated at https://git.aylo.net/aylo/systems/apps/cloudflare-audit
