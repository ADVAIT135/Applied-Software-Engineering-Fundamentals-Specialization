#!/bin/bash

# This checks if the number of arguments is correct
if [[ $# != 2 ]]
then
  echo "backup.sh target_directory_name destination_directory_name"
  exit
fi

# This checks if argument 1 and argument 2 are valid directory paths
if [[ ! -d $1 ]] || [[ ! -d $2 ]]
then
  echo "Invalid directory path provided"
  exit
fi

# [TASK 1]
targetDirectory=$1
destinationDirectory=$2

# [TASK 2]
echo "Target Directory: $targetDirectory"
echo "Destination Directory: $destinationDirectory"

# [TASK 3]
currentTS=$(date +%s)

# [TASK 4]
backupFileName="backup-$currentTS.tar.gz"

# [TASK 5]
origAbsPath=$(pwd)

# [TASK 6]
destAbsPath=$(cd "$destinationDirectory" || exit; pwd)

# [TASK 7]
cd "$targetDirectory" || exit

# [TASK 8]
yesterdayTS=$(($currentTS - 86400))

declare -a toBackup

# [TASK 9]
for file in *; do
  # [TASK 10]
  if [[ $(date -r "$file" +%s) -gt $yesterdayTS ]]; then
    # [TASK 11]
    toBackup+=("$file")
  fi
done

# [TASK 12]
tar -czf "$backupFileName" "${toBackup[@]}"

# [TASK 13]
mv "$backupFileName" "$destAbsPath"

# Congratulations! You completed the final project for this course!