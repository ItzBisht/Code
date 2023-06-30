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