import pandas as pd

df = pd.read_csv("./dataset.csv")
df.columns = df.columns.str.lower()

df0 = df[df["potability"] == 0]
df1 = df[df["potability"] == 1]
df = (
    pd.concat([df0.sample(n=500, random_state=42), df1.sample(n=500, random_state=42)])
    .sample(frac=1, random_state=69)
    .reset_index(drop=True)
)

print(df)
