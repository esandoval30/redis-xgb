# A simple XGBoost Model in RedisAI

This repo contains:
* A fake loan applications dataset (loan-applications.csv). Dataset contains 4499 "records"
    *  8 numerical columns
    *  10 categorical columns
    *  1 target (column to be predicted) with the following values: 
        * 1=Approved 
        * 0=Declined
* A Jupyter notebook with code to:
    * Train an XGB model using the above dataset
    * Convert the trained XGB model to ONNX
    * Visualize the ONNX model
    * Bootstrap 2 tensors in RedisAI required to scale numeric features
* A TorchScript providing feature processing functions to transform all numerical and categorical features into Tensors


## BEFORE YOU START. 
You will need:
* A Redis Server with RedisAI module loaded running on localhost:6349
    * Note: You could use the Dockerfile to create a container image with 
    ``` 
    docker build . 
    ```
* A virtualenv with Python 3.7
    * Activate your virtualenv 
    * install all required python packages with 
    ```
    pip install -r requirements.txt
    ```
* redis-cli

# 1. Start the RedisAI Server (or container)
if you used docker build, grab the container image id and run
```
docker run -p 127.0.0.1:6379:6379/tcp -i -t <imageid>
```

You can get the image id with docker 
```
docker images
```

# 2. Explore (And Run All cells) in the notebook
```
jupyter notebook loan-approval-xgboost-final.ipynb
```

After you run all cells, you will have:
* Bootstrapped 2 tensors (AI.TENSORSET) required to normalize all numerical features
    * xgb-loan-approval-numeric-features-mean
    * xgb-loan-approval-numeric-features-std

* Loaded 10 "loan applications" as Redis hashes
    * loan-application-855
    * loan-application-2561
    * loan-application-2213
    * loan-application-2348
    * loan-application-1530
    * loan-application-800
    * loan-application-600
    * loan-application-1247
    * loan-application-1424
    * loan-application-1400

You will use the model to get predictions on likelihood to be approved for any of the above loans

# 3. Load Feature Processing TorchScript as a RedisAI script

From Terminal run
```
cat feature-processing.py | redis-cli -x AI.SCRIPTSET xgb-loan-approval-feature-processing CPU SOURCE
```

# 4. Load Converted ONNX Model as a RedisAI Model
From Terminal
```
cat pipeline_xgboost_2.onnx | redis-cli -x AI.MODELSTORE xgb-loan-application-model ONNX CPU TAG loan-application:1.0 BLOB
```

# 5. Running a few RedisAI commands
From Terminal
```
redis-cli
```

Once You could try the following commands
## 5.1 Script to normalize numerical features into tensors
```
AI.SCRIPTEXECUTE xgb-loan-approval-feature-processing numeric_values_to_tensors KEYS 1 loan-application-855 INPUTS 3 loan-application-855 xgb-loan-approval-numeric-features-mean xgb-loan-approval-numeric-features-std OUTPUTS 1 loan-application-855-numeric-tensor
```
You could AI.TENSORGET loan-application-855-numeric-tensor to check the resulting tensor!
## 5.2 Script to 1-hot-encode categorical features
```
AI.SCRIPTEXECUTE xgb-loan-approval-feature-processing categorical_values_to_tensors KEYS 1 loan-application-855 INPUTS 1 loan-application-855 OUTPUTS 1 loan-application-855-categorical-tensor
```
You could AI.TENSORGET loan-application-855-categorical-tensor to check the resulting tensor!

## 5.3 Script to pre-process all features in one go
```
AI.SCRIPTEXECUTE xgb-loan-approval-feature-processing pre_process KEYS 1 loan-application-855 INPUTS 3 loan-application-855 xgb-loan-approval-numeric-features-mean xgb-loan-approval-numeric-features-std OUTPUTS 1 loan-application-855-featurized-data
```
You could AI.TENSORGET loan-application-855-featurized-data to check the resulting tensor!

## 5.4 You could get a prediction from the Model
```
AI.MODELEXECUTE xgb-loan-application-model INPUTS 1 loan-application-855-featurized-data OUTPUTS 2 loan-application-855-label loan-application-855-probabilities
```
You could AI.TENSORGET loan-application-855-label to check the predicted outcome (0-Declined ; 1 Approved)








