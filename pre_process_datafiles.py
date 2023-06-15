"""
pre_process_datafiles.py

This script preprocesses the output of 
"""

import pandas as pd
import numpy as np
import sys
import argparse
import os
import pareto
import subprocess

################ Test Case Setup ###################
# Path
header_file = "/Users/marcuslim/Library/CloudStorage/OneDrive-UniversityofCambridge/MPhil_Thesis/Multi-objective Navigation of Radiotherapy Treatment Plan Optimisation Problem/Code/Scripts/header_files/GTV_CTD_Liver_setup_2_header.txt"

input_path = "/Users/marcuslim/Library/CloudStorage/OneDrive-UniversityofCambridge/MPhil_Thesis/Multi-objective Navigation of Radiotherapy Treatment Plan Optimisation Problem/Data/GTV_CTD_Liver/Buti_2022/beam_setup_2/raw_data"
output_path = "/Users/marcuslim/Library/CloudStorage/OneDrive-UniversityofCambridge/MPhil_Thesis/Multi-objective Navigation of Radiotherapy Treatment Plan Optimisation Problem/Data/GTV_CTD_Liver/Buti_2022/beam_setup_2/raw_data"
script_path = os.path.dirname(os.path.realpath(__file__))

#b1_columns = ["b1_0","b1_1","b1_2","b1_3","b1_4","b1_5","b1_6","b1_7","b1_8","b1_9","b1_10","b1_11","b1_12","b1_13","b1_14","b1_15","b1_16","b1_17","b1_18","b1_19","b1_20","b1_21","b1_22","b1_23","b1_24","b1_25","b1_26","b1_27","b1_28","b1_29","b1_30","b1_31","b1_32","b1_33","b1_34","b1_35","b1_36","b1_37","b1_38","b1_39","b1_40","b1_41","b1_42","b1_43","b1_44","b1_45","b1_46","b1_47","b1_48","b1_49","b1_50","b1_51","b1_52","b1_53"]
#b2_columns = ["b2_0","b2_1","b2_2","b2_3","b2_4","b2_5","b2_6","b2_7","b2_8","b2_9","b2_10","b2_11","b2_12","b2_13","b2_14","b2_15","b2_16","b2_17","b2_18","b2_19","b2_20","b2_21","b2_22","b2_23","b2_24","b2_25","b2_26","b2_27","b2_28","b2_29","b2_30","b2_31","b2_32","b2_33","b2_34","b2_35","b2_36","b2_37","b2_38","b2_39","b2_40","b2_41","b2_42","b2_43","b2_44","b2_45","b2_46","b2_47","b2_48","b2_49","b2_50","b2_51","b2_52"]
#b3_columns = ["b3_0","b3_1","b3_2","b3_3","b3_4","b3_5","b3_6","b3_7","b3_8","b3_9","b3_10","b3_11","b3_12","b3_13","b3_14","b3_15","b3_16","b3_17","b3_18","b3_19","b3_20","b3_21","b3_22","b3_23","b3_24","b3_25","b3_26","b3_27","b3_28","b3_29","b3_30","b3_31","b3_32","b3_33","b3_34","b3_35","b3_36","b3_37","b3_38","b3_39","b3_40","b3_41","b3_42","b3_43","b3_44","b3_45","b3_46","b3_47","b3_48","b3_49","b3_50","b3_51","b3_52","b3_53","b3_54"]
b1_columns = ["b1_0","b1_1","b1_2","b1_3","b1_4","b1_5","b1_6","b1_7","b1_8","b1_9","b1_10","b1_11","b1_12","b1_13","b1_14","b1_15","b1_16","b1_17","b1_18","b1_19","b1_20","b1_21","b1_22","b1_23","b1_24","b1_25","b1_26","b1_27","b1_28","b1_29","b1_30","b1_31","b1_32","b1_33","b1_34","b1_35","b1_36","b1_37","b1_38","b1_39","b1_40","b1_41","b1_42","b1_43","b1_44","b1_45","b1_46","b1_47","b1_48","b1_49","b1_50","b1_51","b1_52","b1_53"]
b2_columns = ["b2_0","b2_1","b2_2","b2_3","b2_4","b2_5","b2_6","b2_7","b2_8","b2_9","b2_10","b2_11","b2_12","b2_13","b2_14","b2_15","b2_16","b2_17","b2_18","b2_19","b2_20","b2_21","b2_22","b2_23","b2_24","b2_25","b2_26","b2_27","b2_28","b2_29","b2_30","b2_31","b2_32","b2_33","b2_34","b2_35","b2_36","b2_37","b2_38","b2_39","b2_40","b2_41","b2_42","b2_43","b2_44","b2_45","b2_46","b2_47","b2_48","b2_49","b2_50","b2_51","b2_52","b3_53","b3_54"]
b3_columns = ["b3_0","b3_1","b3_2","b3_3","b3_4","b3_5","b3_6","b3_7","b3_8","b3_9","b3_10","b3_11","b3_12","b3_13","b3_14","b3_15","b3_16","b3_17","b3_18","b3_19","b3_20","b3_21","b3_22","b3_23","b3_24","b3_25","b3_26","b3_27","b3_28","b3_29","b3_30","b3_31","b3_32","b3_33","b3_34","b3_35","b3_36","b3_37","b3_38","b3_39","b3_40","b3_41","b3_42","b3_43","b3_44","b3_45","b3_46","b3_47","b3_48","b3_49","b3_50","b3_51","b3_52","b3_53","b3_54"]

objective_columns = ["Liver","CTD_combined"]
CTD_columns = ["CTD_L0","CTD_CTV","CTD_PTV"]
beamlet_list = [[1, b1_columns],
                [2, b2_columns],
                [3, b3_columns]]

####################################################

################### Functions ######################
def append_columns(dataframe, header_list):
    # Function to append new columns to dataframe to ensure the number of column matches the number of columns
    # stated in the header_list. Obviously, it's expected that the number of columns in header_list should be
    # higher than the number of columns in dataframe.
    # Parameters:
    # - dataframe:		<dataframe> Pandas dataframe to be compared
    # - header_list:	<list> List of headers
    col_diff = len(header_list) - len(dataframe.columns)
    [dataframe.insert(i,i,"") for i in range(len(header_list) - col_diff, len(header_list))]

    return dataset

# Faster than is_pareto_efficient_simple, but less readable.
def is_pareto_efficient(costs, return_mask = True):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :param return_mask: True to return a mask
    :return: An array of indices of pareto-efficient points.
        If return_mask is True, this will be an (n_points, ) boolean array
        Otherwise it will be a (n_efficient_points, ) integer array of indices.
    """
    is_efficient = np.arange(costs.shape[0])
    n_points = costs.shape[0]
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index<len(costs):
        nondominated_point_mask = np.any(costs<costs[next_point_index], axis=1)
        nondominated_point_mask[next_point_index] = True
        is_efficient = is_efficient[nondominated_point_mask]  # Remove dominated points
        costs = costs[nondominated_point_mask]
        next_point_index = np.sum(nondominated_point_mask[:next_point_index])+1
    if return_mask:
        is_efficient_mask = np.zeros(n_points, dtype = bool)
        is_efficient_mask[is_efficient] = True
        return is_efficient_mask
    else:
        return is_efficient
####################################################

###################### Main ########################
if __name__ == "__main__":
    """
    Main section of the pre-processing script

    Each steps of the pre-processing to be run sequentially
    """

    # Here we use subprocess to call the CLI command to run the command to append
    # the filenames to the end of each of the files in the current directory
    # Please take note that the working directory will be pointing to the 
    # directory from which the script is called.

    #print("Running concat filename script")
    #subprocess.run([script_path + "/concat_filename.sh"])
    #subprocess.run([script_path + "/column_arrange.sh"])
    #print("Done running concat filename script")

	# Read the header file
    with open(header_file) as f:
        header_names = f.read().splitlines()

    data_directory = os.fsencode(input_path)

    # Iterate through all files in the data folder
    for file in os.listdir(data_directory):
        if(os.fsdecode(file) == ".DS_Store"):
            continue
        filename = input_path + '/' + os.fsdecode(file)
        print(filename)
        # Read the input file into a dataframe
        dataset = pd.read_csv(filename, header = None)

        # Appending the columns to ensure it matches the number of columns listed in the headers
        dataset = append_columns(dataset, header_names)

        # Assigning the header from the external header files
        dataset.columns = header_names

        # Here we calculate the statistical values of each of the beamlets
        for element in beamlet_list:
            dataset['b{beam_num}_avg'.format(beam_num=element[0])] = dataset.loc[:, element[1]].mean(axis=1)
            dataset['b{beam_num}_max'.format(beam_num=element[0])] = dataset.loc[:, element[1]].max(axis=1)
            dataset['b{beam_num}_min'.format(beam_num=element[0])] = dataset.loc[:, element[1]].min(axis=1)
            dataset['b{beam_num}_std'.format(beam_num=element[0])] = dataset.loc[:, element[1]].std(axis=1)
        print(dataset)

        # Here we calculate the combined objectives value of the CTD
        dataset['CTD_combined'] = dataset.loc[:, CTD_columns].sum(axis=1)

        # Here we call the pareto script to assign the pareto
        objectives_idx = [dataset.columns.get_loc(c) for c in objective_columns if c in dataset]
        print(objectives_idx)
        np_objevtive = dataset.iloc[:, objectives_idx].to_numpy()
        print(np_objevtive)
        #dataset['pareto'] = pareto.flag_nondominated(np_objevtive)
        dataset['pareto'] = is_pareto_efficient(np_objevtive)

        # Saving the dataframe to h
        dataset.to_csv(filename, header=False, index=False)

    # We will use subprocess to call the CLI command to concatenate all the files into a master csv
    #subprocess.run(["concat_content"])
