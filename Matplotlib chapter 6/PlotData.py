import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("./Matplotlib chapter 6/Tears.csv")

ages = data["age"].tolist()
appreciation = data["appreciation"].tolist()

"""
plt.figure()
plt.hist(ages, density=True)
plt.xlabel("Age Bins")
plt.title("Age Histogram")
"""
plt.figure()
plt.scatter(ages, appreciation)
plt.xlabel("Ages")
plt.ylabel("Appreciation")
plt.title("Ages vs. Apprectiation")

plt.show()