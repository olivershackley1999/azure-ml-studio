# Azure ML Studio

Python script for interacting with Azure Machine Learning models via command line arguments.

## Demo

- [Video Walkthrough](https://github.com/user-attachments/assets/9d6984ff-eee9-493c-9ecb-54b9c106d467) - Project overview and usage demonstration

## What it does

- Sends prediction requests to deployed Azure ML endpoints from the command line
- Accepts dynamic input parameters as command line arguments
- Returns formatted model predictions with delay calculations
- Built as part of a flight delay prediction project

## How it works

**Three-step flow:**

1. **Input**: Pass flight parameters (origin, destination, departure, arrival) as command line arguments
2. **API Call**: Script constructs payload and sends POST request to Azure ML endpoint
3. **Output**: Returns raw prediction and calculated delay in human-readable format

## Tech Stack

- Azure Machine Learning (deployed model endpoint)
- Python 3.10+
- Requests library

## Installation

**Prerequisites**: Azure ML workspace with a deployed model endpoint and API key.

1. Clone the repository
   ```bash
   git clone https://github.com/olivershackley1999/azure-ml-studio.git
   cd azure-ml-studio
   ```

2. Install dependencies
   ```bash
   pip install requests
   ```

3. Configure credentials in the script
   ```python
   url = "YOUR_AZURE_ENDPOINT"
   api_key = "YOUR_API_KEY"
   ```

4. Run predictions
   ```bash
   python azure_ml_output.py LAX JFK 800 1600
   ```

## Sample Output

```
Raw Prediction: 1545.23
Predicted Arrival time: 15:45
Delay: 15 minutes delayed
```

## Project Motivation

Built to provide a simple command-line interface for testing deployed Azure ML models, specifically for a flight delay prediction system.
