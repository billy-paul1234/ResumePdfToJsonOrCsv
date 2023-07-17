#!/bin/bash/
#program to remove duplicate headings


h="$(cat "$1"  )"
t=0
        x=0
        while IFS= read -r line ; do
		y=0
	        while IFS= read -r l ; do
			if [ "$line" == "$l" ];then
				t=$(($t+1))
			fi
			if [ $t -eq 2 ];then
				echo "$line" >> "$3"
				break
			fi
        	        y=$(($y+1))
        	done <<< "$h"
		if [ $t -eq 1 ];then
			echo "$line" >> "$2"
		fi
		t=0
		x=$(($x+1))
        done <<< "$h"


