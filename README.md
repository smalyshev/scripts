# scripts
This repo contains scripts used in WDQS maintenance.

- up.sh - Update data on severs
> up.sh [-s "SERVERS1 SERVER2 ..."] ID1 ID2 ...

- onall.sh - Execute command on all servers
> onall.sh [-s "SERVERS1 SERVER2 ..."] command

- check_item.py - check item on all servers to see differences
> python check_item.py QID

- check_servers.py - check query results on all servers. Edit the script to change query.
> python check_servers.py [QID]