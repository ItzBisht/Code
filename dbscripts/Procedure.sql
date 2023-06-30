USE SCHEMA DEMO;

'create or replace procedure employee_validate_json(INPUT VARCHAR)
RETURNS VARIANT NOT NULL
LANGUAGE JAVASCRIPT
AS
$$
var json_row = {};
var error_count = 0;
try {
    var employee_data = JSON.parse(INPUT);
    var employee_id = employee_data.employee_id;
    var employee_name = employee_data.employee_name;
    var employee_address = employee_data.employee_address;
    if (!employee_name) {
        json_row["employee_name"] = "employee name cannot be empty or null.";
        error_count = 1;
    } else {
        var command = "select count(*) from Employee where emp_name='"+ employee_name + "'";
        var stmt = snowflake.createStatement({sqlText: command});
        var res = stmt.execute();
        res.next();
        row_count = res.getColumnValue(1);
    if (row_count > 0) {
        json_row["employee_name"] = "employee name already exists in table.";
        error_count = 1;
    }
}
if (employee_address == null || employee_address == undefined) {
    json_row["employee_address"] = "employee address should not be NULL.";
    error_count = 1;
}
json_row["is_error"] = error_count;
} catch (err) {
    json_row["Exception"] = "Exception: " + err;
    json_row["is_error"] = 1;
}
return json_row;
$$;'