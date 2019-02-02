
import sys

# Reading input file
def reading_data(input_file):

	# Reading input data file (line by line) and make a list
	data_input = open(input_file).read().splitlines()
	data_length = len(data_input) - 1

	# Each line is including inforamtion seprated by ','
	# Extract the information from each line and make a new list
	data_prcd = []
	for data in data_input:
		data_prcd.append(str(data).split(','))

	# Make a list whose each element is a dictionary corresponding to each line
	data_dict = []
	for i in xrange(1, data_length + 1):
		data_dict.append(dict(zip(data_prcd[0], data_prcd[i])))

	return data_dict

# Make a dictionary including:
# 	- drug names (dictionary keys)
# 	- number prescriber and total cost for each drug (dictionary values)
def drug_list(data_dict):
	drugs = {}
	for row in data_dict:
		if row['drug_name'] in drugs:
			drugs[row['drug_name']][0] += 1
			drugs[row['drug_name']][1] += float(row['drug_cost'])
		else:
			drugs[row['drug_name']] = [1 , float(row['drug_cost'])]

	return drugs

# Making output file
def creat_output(output_file, drug_list):
	output_header = 'drug_name,num_prescriber,total_cost'
	with open(output_file, 'w') as file:
		file.write(output_header + '\n')
		for rec in drug_list.keys():
			number = str(drug_list[rec][0])
			cost = str(int(drug_list[rec][1]))
			file.write(rec + ',' + number + ',' + cost + '\n')

	file.close()


if __name__ == "__main__":

	if (len(sys.argv) != 3):
		print 'Please enter input and output file names.'
		sys.exit()
	else:
		input_file = sys.argv[1]
		output_file = sys.argv[2]

	# Reading and pre-procesing data
	data_dict = reading_data(input_file)

	# Finding the number of prescriber and total cost
	drugs = drug_list(data_dict)

	# Make output file
	creat_output(output_file, drugs)


