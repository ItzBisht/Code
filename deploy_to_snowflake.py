import os
import sys
import snowflake.connector

# Retrieve secrets from command-line arguments
snowflake_account = sys.argv[1]
snowflake_user = sys.argv[2]
snowflake_password = sys.argv[3]
snowflake_database = sys.argv[4]
snowflake_schema = sys.argv[5]

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=snowflake_account,
    user=snowflake_user,
    password=snowflake_password,
    database=snowflake_database,
    schema=snowflake_schema
)

# Get a cursor
cursor = conn.cursor()

# Define the path to the directory containing SQL scripts
scripts_dir = "./dbscripts"

# Traverse the directory and execute SQL scripts
for root, dirs, files in os.walk(scripts_dir):
    for file in files:
        if file.endswith(".sql"):
            sql_file = os.path.join(root, file)
            print(f"Executing SQL file: {sql_file}")
            with open(sql_file, "r") as f:
                sql_statements = f.read().split(";")
                for statement in sql_statements:
                    if statement.strip():
                        cursor.execute(statement)

# Close the cursor and connection
cursor.close()
conn.close()