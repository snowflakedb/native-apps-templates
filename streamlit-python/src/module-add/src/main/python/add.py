# This is where you can create python functions, which can further
# be used to create Snowpark UDFs and Stored Procedures in your setup_script.sql file.

# One such example is:
def add_fn(x: int, y: int):
    return x + y