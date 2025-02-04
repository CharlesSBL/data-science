# Import the DuckDB library for database operations
import duckdb

# Step 1: Create a connection to the DuckDB database file
# This creates or opens the database file named 'classification_results.db'
con = duckdb.connect('classification_results.db')

# Step 2: At this point we have a connection object 'con' that lets us:
# - Query data from tables
# - List tables in the database
# - Modify data if the database is not read-only

# Step 3: Query to list all tables in the database
# Using sqlite_master system table to get table names
tables = con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables in the database:", tables)

# Step 4: Attempt to query the classifications table
# Using try/except to handle case where table doesn't exist
try:
    # Execute query to get results as pandas DataFrame
    results = con.execute("SELECT * FROM classifications").df()
    # Print results using DataFrame display
    print("\nClassification results:")
    print(results)
except duckdb.CatalogException as e:
    print(f"\nError: Table 'classifications' not found or other database error: {e}")

# Step 5: Clean up by closing the database connection
# This frees up system resources
con.close()
