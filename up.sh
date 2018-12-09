# Update IDs on all servers
. servers.sh
SERVERS="$EQIAD_MAIN $EQIAD_INT $CODFW_MAIN $CODFW_INT $TEST"
#for s in $SERVERS; do
#  echo ssh $s "cd /srv/deployment/wdqs/wdqs; bash runUpdate.sh -n wdq -N -- --ids $*"
#done
if [ "$1" == '-s' ]; then
  shift
  SERVERS=$1
  shift
fi

pssh -t 0 -p 20 -P -o logs -e elogs -H "$SERVERS" "cd /srv/deployment/wdqs/wdqs; bash runUpdate.sh -n wdq -N -S -- -b 500 --ids $*"
