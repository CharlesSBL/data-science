# data-science

This project showcases two key data science workflows:

1.  **Data Exploration with Pandas:**  We demonstrate how to use the pandas library to read, explore, and manipulate data from a tab-separated file (`01_pop.tsv`).  Specifically, this section covers:

    *   Reading data into a pandas DataFrame using `pd.read_csv(sep='\t')`.
    *   Inspecting the DataFrame: determining its shape (`.shape`), accessing column names (`.columns`), checking data types (`.dtypes`), and getting a summary of the data (`.info()`).
    *   Displaying the first few rows using `.head()`.
    *   Selecting a single column as a pandas Series (e.g., `'country'`) and examining its type.
    *   Creating a new DataFrame by selecting a subset of columns (e.g., `'country'`, `'year'`, `'pop'`).

2.  **Text Classification with Transformers:** We demonstrate using the `transformers` library to classify text using a pre-trained pipeline. This section covers:

    *   Utilizing the `transformers` pipeline for text classification to analyze a sample text (in this case, a complaint letter regarding an incorrect toy shipment).
    *   Storing the classification results (label and score) in a DuckDB database table named `classifications`.
    *   Displaying the stored classifications in a pandas DataFrame for easy viewing.
