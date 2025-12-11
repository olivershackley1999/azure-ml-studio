This Python script enables you to interact with Azure Machine Learning models via command line arguments. 

This was part of a larger project of training a model to predict flight delays. 

I created a brief video that walks through the project here: https://github.com/user-attachments/assets/9d6984ff-eee9-493c-9ecb-54b9c106d467

**Features**
- Interact with Machine Learning models via command line
- Get dynamic model predictions with command line arguments
- Simple, fast way to test deployed endpoints

**Requirements**
- Python 3.10+
- Azure Machine Learning workspace
- A deployed model (Azure provided endpoint)
- An API Key for that endpoint (also Azure provided)

**Usage**

1. Clone the repository: git clone https://github.com/olivershackley1999/azure-ml-studio
2. Add your endpoint URL and API Key where instructed. You can either put them directly inside the script or through environment variables.
3. Run the script: python3 azure_ml_output.py (add applicable command line arguments here)
