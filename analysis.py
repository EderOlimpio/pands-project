import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("iris.csv")

# 1. Save summary statistics to a text file
with open("summary.txt", "w") as f:
    f.write("Iris Dataset Summary\n")
    f.write("=" * 40 + "\n")
    f.write(str(df.describe(include="all")))

# 2. Create output folder if not exists
os.makedirs("images", exist_ok=True)

# 3. Generate histograms for each numeric column
numeric_columns = df.select_dtypes(include="float").columns

for column in numeric_columns:
    plt.figure()
    sns.histplot(df[column], kde=True, bins=15, color="skyblue")
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"images/histogram_{column}.png")
    plt.close()

# 4. Create scatter plot matrix (pairplot)
sns.pairplot(df, hue="species", corner=True)
plt.suptitle("Pair Plot of Iris Features", y=1.02)
plt.savefig("images/pairplot_all.png")
plt.close()

