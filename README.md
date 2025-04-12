# Prices Prediction System

## Overview
The **Prices Prediction System** is a machine learning project designed to predict housing prices using a structured pipeline approach. Built with the ZenML framework for workflow orchestration and MLflow for model tracking and deployment, this repository provides tools to preprocess housing data, train a regression model, and serve predictions. It targets users interested in real estate price forecasting, offering modularity, scalability, and detailed analysis capabilities.

## Features
- **ZenML Pipeline**: Implements a customizable ML pipeline for housing data processing and model training.
- **Model Training & Deployment**: Uses scikit-learn for regression modeling and MLflow for tracking and serving predictions.
- **Housing Price Prediction**: Focuses on predicting house prices based on features like lot size, year built, and living area.
- **Visualization**: Supports data visualization with Matplotlib and Seaborn.
- **Statistical Analysis**: Leverages Statsmodels for advanced modeling.
- **Documentation**: Includes explanations and step-by-step guides.

## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/1111parul/Prices-Prediction-System.git
   cd Prices-Prediction-System
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Install required packages using:
   ```bash
   pip install -r requirements.txt
   ```
   The project depends on:
   - `click==8.1.3`
   - `matplotlib==3.7.5`
   - `mlflow==2.15.1`
   - `mlflow_skinny==2.15.1`
   - `numpy==1.24.4`
   - `pandas==2.0.3`
   - `scikit_learn==1.3.2`
   - `seaborn==0.13.2`
   - `statsmodels==0.14.1`
   - `zenml==0.64.0`

3. **Prepare the Dataset**:
   Place your housing dataset (e.g., CSV with features like `Lot Area`, `Year Built`) in the `data/` directory. Update the pipeline configuration to match your file structure.

## Usage
1. **Run the Pipeline**:
   Execute the ZenML pipeline to process data and train the model:
   ```bash
   python run_pipeline.py
   ```

2. **Make Predictions**:
   Query the MLflow prediction server (running locally at `http://127.0.0.1:8000/invocations`) using:
   ```bash
   python sample_predict.py
   ```
   - Edit `sample_predict.py` with your input data features if needed.
   - Ensure the MLflow server is running (e.g., via `mlflow models serve`).

3. **Deployment**:
   Deploy the system with:
   ```bash
   python run_deployment.py
   ```
   Configure deployment settings in `config.yaml`.

4. **Analysis & Visualization**:
   Explore data and results using scripts in the `analysis/` directory:
   ```bash
   python analysis/<script_name>.py
   ```

*Note*: Refer to script comments or `config.yaml` for additional configuration options.

## Project Structure
```
Prices-Prediction-System/
│
├── .zen/                  # ZenML configuration or metadata
├── __pycache__/           # Python bytecode cache
├── analysis/              # Scripts for data analysis and visualization
├── data/                  # Directory for housing datasets
├── explanations/          # Documentation or explanatory files
├── extracted_data/        # Processed or extracted data
├── mlruns/0/              # MLflow run logs
├── new-repo-dir/          # Sub-project or test directory
├── pipelines/             # Pipeline-related scripts or configurations
├── src/                   # Source code for core functionality
├── steps/                 # Step-by-step process scripts
├── zenml_tutorial/        # ZenML tutorial or example
├── .gitignore             # Git ignore file
├── README.md             # Project documentation
├── config.yaml           # Configuration file
├── mflow.db              # MLflow database
├── requirements.txt      # Python dependencies
├── run_deployment.py     # Deployment script
├── run_pipeline.py       # Pipeline execution script
└── sample_predict.py     # Sample prediction script
```


## Pipeline & Models
The project uses **ZenML (v0.64.0)** to orchestrate a machine learning pipeline, with:
- **Data Preprocessing**: Managed in `pipelines/` or `steps/` using `pandas` and `numpy`.
- **Model Training**: Employs `scikit_learn (v1.3.2)` for a regression model (e.g., Linear Regression or Random Forest) and tracks experiments with `mlflow (v2.15.1)`.
- **Statistical Modeling**: Supports analysis with `statsmodels (v0.14.1)`.
- **Evaluation**: Analysis scripts in `analysis/` generate metrics, visualized with `matplotlib (v3.7.5)` and `seaborn (v0.13.2)`.


```
- **Caching**: Disabled (`enable_cache: False`) for fresh pipeline runs.
- **Docker Integration**: Requires MLflow for containerized deployment.
- **Model Details**: Named `prices_predictor`, licensed under Apache 2.0, focused on housing price prediction.

## Deployment
The `run_deployment.py` script deploys the model, with the `prices_predictor` served via MLflow at `http://127.0.0.1:8000/invocations`. Configure `config.yaml` for deployment settings and ensure the MLflow server is active.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a pull request.

Please follow PEP 8 guidelines and include tests if applicable.

## License
This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details (if present).

## Contact
For questions or suggestions, reach out to the repository owner:
- GitHub: [1111parul](https://github.com/1111parul)

---

1. **Pipeline Execution Overview:** This image illustrates the steps in the ZenML pipeline, from data ingestion to model training and evaluation.
![Screenshot 2025-02-16 1 24 26 PM](https://github.com/user-attachments/assets/7a078636-8ea2-456f-ac41-e551c2d95d51)


2. **Data Preprocessing Steps:** Depicts the preprocessing stage, showing how raw data is cleaned and prepared for model training.
![Screenshot 2025-02-16 1 31 33 PM](https://github.com/user-attachments/assets/7e92b925-3279-4cc2-9a91-b6ff68f70cb2)


3. **Model Training & Evaluation:** Shows the model training process, including hyperparameter tuning and evaluation metrics.
![Screenshot 2025-02-16 1 46 51 PM](https://github.com/user-attachments/assets/f0fb8e68-6833-4099-86ec-aeb58b3bfac1)


4. **MLflow Experiment Tracking:** Visualizes MLflow's interface for tracking experiments, displaying logged parameters and performance metrics.
![Screenshot 2025-02-16 4 47 45 PM](https://github.com/user-attachments/assets/b37882bf-4725-4f27-b41d-7eeb2cda5f78)


5. **Model Versioning with MLflow:** Displays how different model versions are tracked, enabling comparison and selection of the best performing model.
![Screenshot 2025-02-16 4 54 41 PM](https://github.com/user-attachments/assets/6cf32d82-263e-4b54-ba1e-7bf787779eac)


6. **Prediction Results Comparison:** Compares actual vs predicted values to evaluate the model's prediction accuracy.
![Screenshot 2025-02-16 5 01 16 PM](https://github.com/user-attachments/assets/4017bbd4-a22e-4f32-86b8-3075fafd6001)


7. **Model Deployment:** Illustrates the deployment of the model into production, showing how it serves predictions.
![image](https://github.com/user-attachments/assets/61231646-2998-4bcf-9386-3211925fce15)


8. **API Interaction for Predictions:** Shows how users can interact with the deployed model via an API for real-time predictions.
![Screenshot 2025-02-17 7 48 56 PM](https://github.com/user-attachments/assets/727accc5-c178-4aab-97d6-eadacae3cd5b)


9. **Sample Prediction Data:** Displays sample prediction output, showcasing how the system generates price predictions based on input data.
![Screenshot 2025-02-17 7 30 31 PM](https://github.com/user-attachments/assets/b1dd6a76-9bf7-4d69-81bb-569156548a49)


10. **System Architecture Overview:** An architecture diagram of the system, detailing the workflow from data collection to prediction output.
![Screenshot 2025-02-17 7 43 35 PM](https://github.com/user-attachments/assets/63dbeec3-fe5c-4425-9286-e172f47b75d8)








 
