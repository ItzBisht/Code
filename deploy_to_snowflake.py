import os
import snowflake.connector

# Snowflake connection details
account = os.getenv('https://rzlatkv-rf44335.snowflakecomputing.com')
user = os.getenv('HEMADMIN')
password = os.getenv('Fun@12345')
database = os.getenv('DEMO_DB')
schema = os.getenv('DEMO')

# Connect to Snowflake
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema
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