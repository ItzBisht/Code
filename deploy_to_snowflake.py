import os
import snowflake.connector

# Retrieve secrets from environment variables
snowflake_account = os.getenv('SF_ACCOUNT')
snowflake_user = os.getenv('SF_USERNAME')
snowflake_password = os.getenv('SF_PASSWORD')
snowflake_database = os.getenv('SF_DATABASE')
snowflake_schema = os.getenv('SF_SCHEMA')

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

# Deploy SQL scripts
for root, dirs, files in os.walk('./dbscripts'):
    for file in files:
        if file.endswith('.sql'):
            script_path = os.path.join(root, file)
            print(f'Executing SQL file: {script_path}')
            with open(script_path, 'r') as script_file:
                sql_script = script_file.read()
                cursor.execute(sql_script)

# Close the connection
conn.close()