import requests
import json
from datetime import date, datetime
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from requests.api import get

port = 465  # For SSL
smtp_server = "%SMTP Server%"
sender_email = "%FROM ADDRESS%"  # Enter your address
receiver_email = "%TO ADDRESS%"  # Enter receiver address
password = "%PWD%"

date_now = datetime.today().strftime('%Y-%m-%d')
print(date_now)

# Authentication
# Scope = Read All
cloudflare_headers = {
    "Authorization": "Bearer %API TOKEN HERE%",
    "X-Auth-Email": "%ACCOUNT EMAIL HERE%"
}


# Get Zones - Returns a list of CloudFlare Zone IDs. If silent mode is False, a message is shown to the user with the zones and their corrosponding IDs.
def get_zones(silent):
    cloudflare_zones_list = []
    cloudflare_zones_raw = requests.get("https://api.cloudflare.com/client/v4/zones", headers=cloudflare_headers)
    load = json.loads(cloudflare_zones_raw.content)
    zone_response = json.loads(json.dumps(load['result']))
    if len(zone_response) > 0 and silent == False:
        print("The following zones have been found for the account", cloudflare_headers["X-Auth-Email"])
        for zone in zone_response:
            print(zone["name"], "(" + zone["id"] + ")")
            cloudflare_zones_list.append(zone["id"])
    else:
        for zone in zone_response:
            cloudflare_zones_list.append(zone["id"])
        
    return(cloudflare_zones_list)


def get_zone_records(zoneid):
    zone_file_export = open((date_now+"-"+zoneid+".csv"), "w")
    audit_file = open((date_now+"-CloudFlare_Audit.txt"), "a")
    zone_file_export.write("type, name, content, ttl \n")
    audit_file.write("--------------------------------------------------------------------\n")
    audit_file.write("Domain Records for: " + zoneid + "\n")
    audit_file.write("--------------------------------------------------------------------\n")
    audit_file.write("type, name, content, ttl \n")
    domain_zone_response = json.loads(requests.get("https://api.cloudflare.com/client/v4/zones/"+zoneid+"/dns_records?per_page=100", headers=cloudflare_headers).content)
    domain_zone_response_data = json.loads(json.dumps(domain_zone_response['result']))
    for record in domain_zone_response_data:
        record_string = record["type"]+","+record["name"]+","+record["content"]+","+str(record["ttl"])+"\n"
        zone_file_export.write(record_string)
        audit_file.write(record_string)
    zone_file_export.close
    audit_file.close

def main():
    zones = get_zones(True)
    for zone in zones:
        get_zone_records(zone)
    print("Done")

def send_mail():
    audit_file = open(date_now+"-CloudFlare_Audit.txt", "r")
    audit_file_txt = audit_file.read()
    message = MIMEMultipart("alternative")
    message["Subject"] = ("CloudFlare Audit - " + date_now)
    message["From"] = sender_email
    message["To"] = reviever_email

    part1 = MIMEText(audit_file_txt, "plain")
    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

main()
send_mail()
