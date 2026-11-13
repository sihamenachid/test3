import pandas as pd
from shapes import Circle, Rectangle

shapes = [Circle(2), Rectangle(3, 4), Circle(1)]
data = [{"type": type(s).__name__, "area": round(s.area(), 2)} for s in shapes]

df = pd.DataFrame(data)
print(df)
df.to_csv("areas.csv", index=False)
print("Mean area:", df["area"].mean())