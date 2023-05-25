 #! /bin/bash

 echo "Enter problem name"
 read problemName

 mkdir -p $problemName

#Sync

cp rider-sharing/geektrust.py template/
cp rider-sharing/src/utils.py template/src/
find rider-sharing/tests -type f ! -name "*rider*" -name "*.py" -exec cp {} "template/tests" \;
cp rider-sharing/*.sh template/
cp rider-sharing/requirements.txt template/

#Copy template files
cp -r template/*  $problemName/

 cd "$problemName"

# Use sed to replace ProblemName with the problem namereplace hyphen with space and capitalize the words
title=$(echo "$problemName" | sed 's/-/ /g; s/\b\([a-z]\)/\u\1/g')

echo $title


sed  "s/\[ProblemName\]/$title/g"  readme.md > readme.md.tmp
mv readme.md.tmp readme.md

touch $problemName.ipynb