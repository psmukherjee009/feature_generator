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
Build a simple reusable general purpose feature generator for general Machine Learning use.

## Feature Definition
The feature master file are the .schema file which defines the Raw data and the features. This file provides
 feature generator a map of what is expected raw data and features.
#### Raw Data
 1:1 mapping of raw data columns. This only contains the feature name and must be declared before any computed feature 
 is defined
 
#### Features
This part defines the feature as a name value pair. The feature name is one word. Rest of the string(value) 
describes how to compute the feature. The value could be a python expression or a python function call. 
Like:-
 
```bash

import feat
# Raw Data -- A comment which will be ignored by the system
 Open                                float(S_Open[0])
  
 Atr                                 feat.atr(High, Low, Close)

```

 To call external python function, you need to include the file using `import feat` in the case above before any
 external call is made.
 
 