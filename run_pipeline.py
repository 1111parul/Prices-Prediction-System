import click
from pipelines.training_pipeline import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri


@click.command()
def main():
    """
    Run the ML pipeline and start the MLflow UI for experiment tracking.
    """
    # Run the pipeline
    run = ml_pipeline()

    # You can uncomment and customize the following lines if you want to retrieve and inspect the trained model:
    # trained_model = run["model_building_step"]  # Replace with actual step name if different
    # print(f"Trained Model Type: {type(trained_model)}")

    print(
        "Now run \n "
        f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
        "To inspect your experiment runs within the mlflow UI.\n"
        "You can find your runs tracked within the experiment."
    )


if __name__ == "__main__":
    main()





# import click
# import mlflow
# from pipelines.training_pipeline import ml_pipeline
# from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri


# @click.command()
# def main():
#     """
#     Run the ML pipeline and start the MLflow UI for experiment tracking.
#     """
#     print("🚀 Running the ML pipeline...")

#     # Start MLflow run to track execution
#     with mlflow.start_run(run_name="training_run"):
#         # Execute the ML pipeline
#         run = ml_pipeline()

#     print("✅ Training pipeline completed successfully!")

#     print(
#         "📊 Now run the following command to inspect experiment runs in MLflow UI:\n"
#         f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
#         "🔗 Open http://127.0.0.1:5000 in your browser to view logs and metrics."
#     )


# if __name__ == "__main__":
#     main()
