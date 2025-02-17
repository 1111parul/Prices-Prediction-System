from steps.data_ingestion_step import data_ingestion_step
from steps.data_splitter_step import data_splitter_step
from steps.feature_engineering_step import feature_engineering_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.model_building_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step
from steps.outlier_detection_step import outlier_detection_step
from zenml import Model, pipeline, step


@pipeline(
    model=Model(
        # The name uniquely identifies this model
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    raw_data = data_ingestion_step(
        file_path="//home/prarthanaparul625/prices-predictor-system/data/archive.zip"
    )

    # Handling Missing Values Step
    filled_data = handle_missing_values_step(raw_data)

    # Feature Engineering Step
    engineered_data = feature_engineering_step(
        filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )

    # Outlier Detection Step
    clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")

    # Data Splitting Step
    X_train, X_test, y_train, y_test = data_splitter_step(clean_data, target_column="SalePrice")

    # Model Building Step
    model = model_building_step(X_train=X_train, y_train=y_train)

    # Model Evaluation Step
    evaluation_metrics, mse = model_evaluator_step(
        trained_model=model, X_test=X_test, y_test=y_test
    )

    return model


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()






# from steps.data_ingestion_step import data_ingestion_step
# from steps.data_splitter_step import data_splitter_step
# from steps.feature_engineering_step import feature_engineering_step
# from steps.handle_missing_values_step import handle_missing_values_step
# from steps.model_building_step import model_building_step
# from steps.model_evaluator_step import model_evaluator_step
# from steps.outlier_detection_step import outlier_detection_step
# from zenml import Model, pipeline, step
# import mlflow
# import mlflow.sklearn  # Ensure MLflow supports scikit-learn models
# import os

# # Set MLflow experiment
# mlflow.set_experiment("Prices_Predictor")

# @pipeline(
#     model=Model(name="prices_predictor"),
# )
# def ml_pipeline():
#     """End-to-end ML pipeline with MLflow tracking."""
    
#     with mlflow.start_run():
#         # Data Ingestion Step
#         raw_data = data_ingestion_step(
#             file_path="//home/prarthanaparul625/prices-predictor-system/data/archive.zip"
#         )

#         # Handling Missing Values
#         filled_data = handle_missing_values_step(raw_data)

#         # Feature Engineering
#         engineered_data = feature_engineering_step(
#             filled_data, strategy="log", features=["Gr Liv Area", "SalePrice"]
#         )

#         # Outlier Detection
#         clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")

#         # Data Splitting
#         X_train, X_test, y_train, y_test = data_splitter_step(clean_data, target_column="SalePrice")

#         # Model Training
#         model = model_building_step(X_train=X_train, y_train=y_train)

#         # Log model hyperparameters (customize as per your model)
#         mlflow.log_param("model_type", "RandomForest")  # Example model type
#         mlflow.log_param("data_split_ratio", "80-20")

#         # Model Evaluation
#         evaluation_metrics, mse = model_evaluator_step(trained_model=model, X_test=X_test, y_test=y_test)

#         # Log evaluation metrics
#         mlflow.log_metric("MSE", mse)

#         # Save & log model artifact
#         model_path = "artifacts/prices_predictor.pkl"
#         os.makedirs("artifacts", exist_ok=True)
#         mlflow.sklearn.save_model(model, model_path)
#         mlflow.log_artifact(model_path)

#         return model


# if __name__ == "__main__":
#     # Running the pipeline
#     run = ml_pipeline()
