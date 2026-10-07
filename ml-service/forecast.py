from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

DATA_FILE = Path(__file__).parent / "sales.csv"


def forecast_next_month() -> float:
    df = pd.read_csv(DATA_FILE)
    if not {"month", "sales"}.issubset(df.columns):
        raise ValueError("sales.csv must contain month and sales columns")

    x = df[["month"]]
    y = df["sales"]
    model = LinearRegression()
    model.fit(x, y)
    next_month = int(df["month"].max()) + 1
    prediction = float(model.predict([[next_month]])[0])
    return prediction


if __name__ == "__main__":
    value = forecast_next_month()
    print(f"Predicted sales for next month: {value:.2f}")
