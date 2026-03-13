from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yaml
from sklearn.tree import plot_tree

from src.data.load_data import load_train_test
from src.data.preprocess import preprocess_data
from src.features.build_features import encode_target, get_feature_types, split_features
from src.models.evaluate_model import evaluate_model
from src.models.predict_model import make_predictions
from src.models.train_model import train_model
from src.pipelines.training_pipeline import create_training_pipeline
from src.utils.helper import ensure_dir, project_root


def load_config(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def plot_and_save_confusion_matrix(cm, output_path: Path) -> None:
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_and_save_feature_importance(model_pipeline, output_path: Path) -> None:
    model = model_pipeline.named_steps["model"]
    preprocessor = model_pipeline.named_steps["preprocessor"]

    feature_names = preprocessor.get_feature_names_out()
    importances = model.feature_importances_

    fi = pd.DataFrame({"feature": feature_names, "importance": importances})
    fi = fi.sort_values("importance", ascending=False).head(20)

    plt.figure(figsize=(10, 7))
    sns.barplot(data=fi, x="importance", y="feature", palette="viridis")
    plt.title("Top 20 Feature Importances")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_and_save_tree_visual(model_pipeline, output_path: Path) -> None:
    model = model_pipeline.named_steps["model"]
    preprocessor = model_pipeline.named_steps["preprocessor"]
    feature_names = preprocessor.get_feature_names_out()

    plt.figure(figsize=(22, 10))
    plot_tree(
        model,
        max_depth=3,
        feature_names=feature_names,
        class_names=["<=50K", ">50K"],
        filled=True,
        fontsize=8,
    )
    plt.title("Decision Tree Visualization (Depth <= 3)")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def write_report(metrics: dict, output_path: Path, model_params: dict) -> None:
    report_text = (
        "# Adult Income Decision Tree Report\n\n"
        "## Model\n"
        f"- Algorithm: DecisionTreeClassifier\n"
        f"- Parameters: {model_params}\n\n"
        "## Metrics\n"
        f"- Accuracy: {metrics['accuracy']:.4f}\n\n"
        "## Classification Report\n"
        "```\n"
        f"{metrics['classification_report']}\n"
        "```\n"
    )
    output_path.write_text(report_text, encoding="utf-8")


def main() -> None:
    root = project_root()
    config = load_config(root / "config" / "model_config.yaml")

    paths = config["paths"]
    model_params = config["model"]
    target_col = config["target_column"]

    train_path = root / paths["train_data"]
    test_path = root / paths["test_data"]
    processed_path = root / paths["processed_data"]
    model_path = root / paths["model_output"]
    report_path = root / paths["report_output"]
    cm_fig = root / paths["confusion_matrix_fig"]
    fi_fig = root / paths["feature_importance_fig"]
    tree_fig = root / paths["tree_visualization_fig"]

    ensure_dir(processed_path.parent)
    ensure_dir(model_path.parent)
    ensure_dir(report_path.parent)
    ensure_dir(cm_fig.parent)

    train_df, test_df = load_train_test(str(train_path), str(test_path))
    train_df = preprocess_data(train_df)
    test_df = preprocess_data(test_df)

    # Save cleaned train set for re-use and traceability.
    train_df.to_csv(processed_path, index=False)

    X_train, y_train = split_features(train_df, target_col)
    X_test, y_test = split_features(test_df, target_col)

    y_train = encode_target(y_train)
    y_test = encode_target(y_test)

    categorical_features, numerical_features = get_feature_types(X_train)

    pipeline = create_training_pipeline(categorical_features, numerical_features, model_params)
    trained_model = train_model(pipeline, X_train, y_train)

    y_pred = make_predictions(trained_model, X_test)
    metrics = evaluate_model(y_test, y_pred)

    joblib.dump(trained_model, model_path)
    plot_and_save_confusion_matrix(metrics["confusion_matrix"], cm_fig)
    plot_and_save_feature_importance(trained_model, fi_fig)
    plot_and_save_tree_visual(trained_model, tree_fig)
    write_report(metrics, report_path, model_params)

    print("Training complete.")
    print(f"Model: {model_path}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
