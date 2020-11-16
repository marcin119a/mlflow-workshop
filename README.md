## mlflow


```bash
pip install -r requirements.txt
```

```
 mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root .
```

```
mflow ui
```

```
mlflow run -e main git@github.com:marcin119a/mlflow-workshop.git
```