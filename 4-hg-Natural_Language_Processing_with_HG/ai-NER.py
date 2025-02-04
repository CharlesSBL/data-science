
# Import JSON library for reading the input file
import json

# Read the JSON file
with open('text.json', 'r') as file:
    text_data = json.load(file)

# Import and initialize the NER pipeline from transformers
from transformers import pipeline
ner_tagger = pipeline("ner", aggregation_strategy="simple", device="cpu", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# ----==----==----==----==----==----==----==----==----

# Import required data handling libraries
import pandas as pd
import duckdb

# Run NER on each text and combine results into DataFrame
all_outputs = []
for text in text_data['text']:
    try:
        # Print text being processed for debugging
        print(f"\nProcessing text: {text}")

        outputs = ner_tagger(text)
        if outputs:  # Only add if there are actual entities found
            if isinstance(outputs, (list, pd.DataFrame)):
                all_outputs.extend(outputs)
            else:
                all_outputs.append(outputs)
    except Exception as e:
        print(f"Error processing text: {text}")
        print(f"Error: {str(e)}")
        continue

df = pd.DataFrame(all_outputs)

# Print number of entities found
print(f"\nTotal entities found: {len(df)}")

# ----==----==----==----==----==----==----==----==----

# Initialize connection to DuckDB database
con = duckdb.connect('classification_results.db')

# Create a table if it doesn't exist and insert the NER results
con.execute('''
    CREATE TABLE IF NOT EXISTS classifications (
        entity_group VARCHAR,
        word VARCHAR,
        score DOUBLE,
        start_pos INTEGER,
        end_pos INTEGER
    )
''')

# Convert DataFrame columns to appropriate types before insert
if not df.empty:
    df['score'] = pd.to_numeric(df['score'])
    df['start'] = pd.to_numeric(df['start'])
    df['end'] = pd.to_numeric(df['end'])

    # Insert data
    con.execute('INSERT INTO classifications SELECT entity_group, word, score, start as start_pos, "end" as end_pos FROM df')

# Close the database connection
con.close()

# Display the NER results
print("\nClassification results:")
print(df)
