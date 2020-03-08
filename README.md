## Requirement
python3

## TestDrive
After cloning the repo, run
```bash
chmod +x run.sh
./run.sh
```
OR
```bash
python3 gen_features.py -p -s v1_features.schema SPY.csv
```

## Objective
Build a simple reusable general purpose feature generator for Machine Learning.

## Feature Definition
The feature master file is the .schema file which defines the Raw data and the features. This file provides
 feature generator a map of what is expected raw data and generated features.
 
#### Raw Data
1:1 mapping of raw data columns with schema raw columns. Raw Data columns must be declared before any computed feature uses them.
 
#### Features
Feature are defined as name value pair. The feature name is one word. Rest of the string(value) 
describes how to compute the feature. The value could be a python expression or a python function call. 
Like:-
 
```bash

import feat

# Raw Data -- A comment which will be ignored by the system
S_Open
S_High
S_Low
S_Close
S_Volume

# Features
# Value computed using python expression
 Open                                float(S_Open)
 High                                float(S_High)
 Low                                 float(S_Low)
 Close                               float(S_Close)
 Volume                              float(S_Volume)
 
 # Value computed using an outside function call
 Atr                                 feat.atr(High, Low, Close)

```

 To call external python function, you need to include the file, using `import feat` in the case above, before any
 external call is made.
 
 
