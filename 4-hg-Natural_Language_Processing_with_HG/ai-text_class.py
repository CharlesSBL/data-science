# Define the sample text - a complaint letter about a toy mix-up
text = """Dear Amazon, last week I ordered an Optimus Prime action figure
from your online store in Germany. Unfortunately, when I opened the package,
I discovered to my horror that I had been sent an action figure of Megatron
instead! As a lifelong enemy of the Decepticons, I hope you can understand my
dilemma. To resolve the issue, I demand an exchange of Megatron for the
Optimus Prime figure I ordered. Enclosed are copies of my records concerning
this purchase. I expect to hear from you soon. Sincerely, Bumblebee."""

# Import and initialize the text classification pipeline from transformers
from transformers import pipeline
classifier = pipeline("text-classification")

# ----==----==----==----==----==----==----==----==----

# Import required data handling libraries
import pandas as pd
import duckdb

# Run the classifier on our text and convert results to DataFrame
outputs = classifier(text)
df = pd.DataFrame(outputs)

# ----==----==----==----==----==----==----==----==----

# Initialize connection to DuckDB database
con = duckdb.connect('classification_results.db')

# Create a table if it doesn't exist and insert the classification results
con.execute('CREATE TABLE IF NOT EXISTS classifications (label VARCHAR, score DOUBLE)')
con.execute('INSERT INTO classifications SELECT * FROM df')

# Close the database connection
con.close()

# Display the classification results
print(df)
