import csv
with open('iowa-liquor-sample.csv') as csvfile:
	reader = csv.reader(csvfile)
	SCOTCH_NAME = "single malt scotch"
	count = 0
	for row in reader:
		row_string = ", ".join(row)
		row_string_lower = row_string.lower()
		if SCOTCH_NAME in row_string_lower:
			count += 1
	print "Number of", SCOTCH_NAME, ":", count