#!/bin/sh
# FILE='testfile'
IFS_OLD=$IFS
IFS=$'\n'
echo $2:0-2
for line in `cat $1`
do
	IFS=$IFS_OLD
	for word in `echo $line`
	do
		echo $word
	done
done
