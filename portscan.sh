for x in {1..65000};
do
	(echo </dev/tcp/$1/$x "Port $x Opened......") 2>/dev/null;
done
