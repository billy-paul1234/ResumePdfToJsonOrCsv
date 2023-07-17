#!/bin/bash/
#program to convert heading.txt to smaller case.


apps="$(cat /home/billy/Desktop/programing/python/restum2csv/heading.txt  )"
echo $apps

        x=0
        while IFS= read -r line ; do
		echo "$(echo "$line" | tr '[:upper:]' '[:lower:]' )" >> d.txt
                x=$(($x+1))
                echo  "p_'$line'"
        done <<< "$apps"

