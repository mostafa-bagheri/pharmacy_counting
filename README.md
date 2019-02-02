# Table of Contents
1. [Project Title](README.md#project-title)
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Output](README.md#output)
1. [Algorithm](README.md#algorithm)
1. [Questions?](README.md#questions?)


# Project Title

Insight Data Engineering Pharmacy Counting Coding Challenge


# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 


# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 


# Output 

This program creates the output file, `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file contains these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers


# Algorithm

ّFirst, input data file (line by line) was read and a list was made (`data_input`).
For example, one element of list is:

    1000000003,Johnson,James,CHLORPROMAZINE,1000

Then, information extracted from each line and a list of lists was made (`data_prcd`):
    
    ['1000000003', 'Johnson', 'James', 'CHLORPROMAZINE', '1000']

Finally, a list of dictionary from each line was made (`data_dict`):
    
    {'drug_name': 'CHLORPROMAZINE', 'drug_cost': '2000', 'id': '1000000004',
    'prescriber_last_name': 'Rodriguez', 'prescriber_first_name': 'Maria'}

Afterward, I made a dictionary (`drugs`) which gets the name of each drug (key), and the number of prescribers and total cost (value). To this end, I read the dictionaries one by one in `data_dict` and update the `drugs` dictionary.

Finally, each item in the dictionary (`drugs`) was writen line by line.

***'sys' was the only library which I used.***


# Questions?
Email us at mstfbagheri@ucsd.edu
