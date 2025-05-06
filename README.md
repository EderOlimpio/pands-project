
# pands-project

## Programming and Scripting Project – Analysis of the Iris Dataset using Python

### Author
Eder Olimpio

---

## Dataset Information

The dataset used in this project is the Iris dataset, first introduced by the British statistician and biologist Ronald Fisher in 1936.

It contains 150 observations across three species of iris flowers:
- Iris-setosa
- Iris-versicolor
- Iris-virginica

Each observation includes four numerical features:
- Sepal length
- Sepal width
- Petal length
- Petal width

This dataset is widely used for data visualization and machine learning tutorials due to its simplicity and balanced class distribution.

---

## Project Structure

This project performs an exploratory data analysis (EDA) of the Iris dataset using Python. It includes:

- Summary statistics
- Histograms of each numeric variable
- A scatterplot matrix (pairplot)
- A correlation heatmap

### Files:
- `iris.csv` — Dataset file
- `analysis.py` — Main script performing the analysis
- `summary.txt` — Text summary of statistics
- `images/` — Contains:
  - Histograms (`histogram_*.png`)
  - Pairplot (`pairplot_all.png`)
  - Correlation heatmap (`heatmap_correlation.png`)

---

## How to Run

1. **Install Required Libraries**  

   Open your terminal and run:

   ```bash
   pip install pandas matplotlib seaborn```

1. **Run the Analysis Script**

  In the terminal, run:

  ```bash
  python analysis.py
  ```

  This will:

- Print summary statistics to the console

- Save a text file (```summary.txt```) with the statistics

- Generate plots in the ```images/``` directory

---

## Analysis Performed

1. **Summary Statistics**

- Uses ```pandas.describe()``` to calculate count, mean, standard deviation, min, max, and percentiles for all numeric columns.

2. **Histograms**

- One histogram per numeric variable using ```seaborn.histplot()```.

- Shows the distribution of values for each feature across all species.

3. **Pairplot (Scatterplot Matrix)**

- Created with ```seaborn.pairplot()```.

- Visualizes the relationships between all pairs of numeric features.

- Colored by species to reveal class separation.

4. **Correlation Heatmap**

- Created using ```seaborn.heatmap()``` and ```df.corr()```.

- Displays the correlation coefficients between each pair of numeric variables.

- Reveals strong correlations like petal length and petal width.

---

## Insights and Conclusions

- Petal length and petal width are strongly positively correlated.

- Setosa species is clearly separable from the others using petal dimensions.

- Sepal measurements show more overlap across species, making them less reliable for classification.

- This supports the use of petal features in classification models.

## Summary

- This project demonstrates how to:

- Import and manipulate data using pandas

- Perform basic statistical analysis

- Generate meaningful data visualizations using seaborn and matplotlib

- Save output to files and structure a Python analysis script professionally
