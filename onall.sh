# Update IDs on all servers
. servers.sh
SERVERS="$SERVERS $TEST"
if [ "$1" == '-s' ]; then
  shift
  SERVERS=$1
  shift
fi
pssh -x -t -p 15 -o logs -e elogs -H "$SERVERS" "$*"
