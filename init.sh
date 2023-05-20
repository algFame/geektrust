 #!/bin/bash

 echo "Enter problem name"
 read problemName

 mkdir -p $problemName

 cp -r template/*  $problemName/

sed  's/\[ProblemName\]/$problemName/g' template/readme.md
