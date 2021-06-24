# Remember to add execution rights with chmod +x ./cron-job-dns-audit.sh

#!/bin/bash
python3 /opt/aylo/cloudflare-audit/audit-cloudflare.py
echo "[$(date +"%F %T")] Job Run Cloudflare Audit (python3 /opt/aylo/cloudflare-audit/audit-cloudflare.py)" >> /var/log/%LOG NAME%.log
