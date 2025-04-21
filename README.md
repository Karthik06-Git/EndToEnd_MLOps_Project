# EndToEnd_MLOps_Project


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the Configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py







# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Karthik06-Git/EndToEnd_MLOps_Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.11 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up your local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


MLFLOW_TRACKING_URI= https://dagshub.com/Karthik06-Git/EndToEnd_MLOps_Project.mlflow \
MLFLOW_TRACKING_USERNAME= Karthik06-Git  \
MLFLOW_TRACKING_PASSWORD= a3cb112c9d5517810f14bf35658ea4d8abb54d97 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Karthik06-Git/EndToEnd_MLOps_Project.mlflow

export MLFLOW_TRACKING_USERNAME=Karthik06-Git

export MLFLOW_TRACKING_PASSWORD=a3cb112c9d5517810f14bf35658ea4d8abb54d97

```

if 'export' commands doesn't work use 'set':

```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/Karthik06-Git/EndToEnd_MLOps_Project.mlflow

set MLFLOW_TRACKING_USERNAME=Karthik06-Git

set MLFLOW_TRACKING_PASSWORD=a3cb112c9d5517810f14bf35658ea4d8abb54d97

```