EQIAD_MAIN="wdq3 wdq4 wdq5"
EQIAD_INT="wdq6 wdq7 wdq8"
CODFW_MAIN="wdq21 wdq22 wdq23"
CODFW_INT="wdq24 wdq25 wdq26"
TEST="wdq9 wdq10"
SERVERS="$EQIAD_MAIN $EQIAD_INT $CODFW_MAIN $CODFW_INT"

get_server() {
	if [ "$1" == '-s' ]; then
	  shift
	  SERVERS=$1
	  shift
	fi
}
