#!/bin/bash
file="productCategories.txt"
name=$(cat "$file")
for variable in $name
do 
	echo "Downloading reviews for category:::${variable}"
	wget http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/${variable}_5.json.gz
done
