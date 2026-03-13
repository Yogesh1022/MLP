# Adult Income Decision Tree

End-to-end Decision Tree classification project for the Adult Income dataset.

## Project structure

- data/raw: original Adult dataset files
- data/processed: cleaned dataset output
- notebooks: exploratory analysis notebook
- src: training/evaluation source code
- models: serialized trained pipeline
- reports: evaluation report and plots
- config: model and path configuration

## Run training

```bash
python main.py
```

## Outputs generated

- models/decision_tree_pipeline.pkl
- data/processed/cleaned_data.csv
- reports/model_report.md
- reports/figures/confusion_matrix.png
- reports/figures/feature_importance.png
- reports/figures/decision_tree_visualization.png
