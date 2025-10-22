# EndToEnd_MLOps_Project

Deployed a Car Price Prediction Web App using Flask and AWS-EC2, integrated with a CI/CD pipeline via GitHub Actions.
The model predicts prices of old cars based on user inputs like brand, fuel_type, kilometer_driven and ownership details.
Built with a custom MLOPs pipeline, Docker containerization, and secure AWS deployment for scalability.


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



### Deployment link :-

```bash
http://54.147.201.86:8080/
```




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Karthik06-Git/EndToEnd_MLOps_Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python==3.11 -y
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




# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 891377245898.dkr.ecr.us-east-1.amazonaws.com/mlops-project

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optional

	sudo apt-get update -y

	sudo apt-get upgrade -y
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
## 6. Configure EC2 as self-hosted runner (from GitHub):
    setting > actions > runner > new self hosted runner > choose os > then run command one by one


## 7. Setup github secrets:

    AWS_ACCESS_KEY_ID = ****

    AWS_SECRET_ACCESS_KEY = ****

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>> 891377245898.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = mlops-project






## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model




## Web Screenshots

1) Web-App before filling details
![image1](https://github.com/Karthik06-Git/EndToEnd_MLOps_Project/blob/main/web_screenshots/image-01.png)

2) Web-App after filling details 
![image1](https://github.com/Karthik06-Git/EndToEnd_MLOps_Project/blob/main/web_screenshots/image-02.png)

3) Result page 
![image1](https://github.com/Karthik06-Git/EndToEnd_MLOps_Project/blob/main/web_screenshots/image-03.png)