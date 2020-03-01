#!/usr/bin/env bash

# Generate Features
python3 gen_features.py -p -s v1_features.schema SPY.csv > SPY_features.csv
