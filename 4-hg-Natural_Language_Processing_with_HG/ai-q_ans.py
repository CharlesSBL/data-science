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
reader = pipeline("question-answering")
question = "What does the customer want?"

# ----==----==----==----==----==----==----==----==----

# Import required data handling libraries
import pandas as pd
import duckdb

# Run the classifier on our text and convert results to DataFrame
outputs = reader(question=question, context=text)
df = pd.DataFrame([outputs])

# Convert start/end positions to integers explicitly
df['start'] = df['start'].astype(int)
df['end'] = df['end'].astype(int)

# ----==----==----==----==----==----==----==----==----

# Initialize connection to DuckDB database
con = duckdb.connect('classification_results.db')

# Create a table if it doesn't exist and insert the classification results
con.execute('CREATE TABLE IF NOT EXISTS classifications (answer VARCHAR, score DOUBLE, start_pos INTEGER, end_pos INTEGER)')
con.execute('''INSERT INTO classifications
               SELECT answer, score, "start" as start_pos, "end" as end_pos
               FROM df''')

# Close the database connection
con.close()

# Display the classification results
print(df)
