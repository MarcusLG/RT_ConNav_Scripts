"""
pre_process_datafiles.py

This script preprocesses the output of 
"""

import pandas as pd
import sys
import argparse
import os

header_file = "/Users/marcuslim/Library/CloudStorage/OneDrive-UniversityofCambridge/MPhil_Thesis/Multi-objective Navigation of Radiotherapy Treatment Plan Optimisation Problem/Code/Scripts/header_files/GTV_CTD_Liver_header.txt"
input_file = "/Users/marcuslim/Library/CloudStorage/OneDrive-UniversityofCambridge/MPhil_Thesis/Multi-objective Navigation of Radiotherapy Treatment Plan Optimisation Problem/Data/GTV_CTD_Liver/Buti_2022/Raw_Data/100_15_05"

if __name__ == "__main__":
    with open(header_file) as f:
        header_names = f.read().splitlines()
    dataset = pd.read_csv(input_file)
    dataset.columns = header_names