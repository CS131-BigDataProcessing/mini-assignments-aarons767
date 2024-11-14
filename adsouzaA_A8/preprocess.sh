#!/bin/bash

echo "Searching for missing values"

# Searching for missing values and logging them
awk -F, '{
  for (i=1; i<=NF; i++) {
    if ($i == "" || $i ~ /^ *$/) {
      print "Missing value found in row " NR " column " i;
    }
  }
}' "./AB_NYC_2019.csv" > "./missing_values_report.txt"

echo "Removing rows with missing values"

# Removing rows with consecutive commas, suggesting missing values
sed '/,,/d' "./AB_NYC_2019.csv" > "./clean_data_no_missing.csv"
sed 's/,,/,NA,/g' "./AB_NYC_2019.csv" > "./clean_data_with_NA.csv"

echo "Removing duplicate entries"

# Removing duplicates
sort "./AB_NYC_2019.csv" | uniq > "./clean_data_no_duplicates.csv"

echo "Calculating mean and median"

# Define the file path
file_path="./AB_NYC_2019.csv"

# Calculating mean price
mean_price=$(awk -F, 'NR > 1 {sum += $10; count++} END {print sum / count}' "$file_path")

median_price=$(awk -F, 'NR > 1 {print $10}' "$file_path" | sort -n | awk '{
  count[NR] = $1;
}
END {
  if (NR % 2 == 1) {
    median = count[(NR + 1) / 2];
  } else {
    median = (count[NR / 2] + count[(NR / 2) + 1]) / 2;
  }
  print median
}')


# Output results
echo "Mean price: $mean_price" > ./price_statistics.txt
echo "Median price: $median_price" >> ./price_statistics.txt

echo "Results saved to price_statistics.txt."
