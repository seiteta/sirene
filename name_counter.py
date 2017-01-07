#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:33:09 2017

@author: seiteta
"""
import pandas as pd

# NB: the original csv file has been re-encoded with the following bash command:
# `iconv -f ISO-8859-15 -t utf-8 sirc-17804_9075_14209_201612_L_M_20170104_171522721.csv > sirc-utf8.csv`

# Read only the "PRENOM" columns of the files
prenoms = pd.read_csv("sirc-utf8.csv", delimiter = ";",
                      dtype = {"PRENOM": str}, usecols=['PRENOM'], squeeze = True)

# Count the first names
prenom_rank = prenoms.value_counts()

# Convert the Series into a DataFrame
prenom_rank = prenom_rank.to_frame()
prenom_rank.reset_index(inplace=True)
prenom_rank.columns = ['prenom', 'count']

# Compute first name frequency
prenom_rank['frequency'] = 100* prenom_rank['count']/(prenom_rank['count'].sum())

# Export the first name ranking
prenom_rank.to_csv("prenoms.csv", index = None)
