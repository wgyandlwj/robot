import hashlib

grid_zie = 10

name = input("What is the name of the robot?")
identifier = hashlib.sha256(name.encode()).hexdigest()

row_index = int(input("Enter current row index: "))
column_index = int(input("Enter current column index: "))
valid_row_index = max(min(row_index, grid_zie - 1), 0)
valid_column_index = max(min(column_index, grid_zie - 1), 0)
if valid_column_index >= 5:
    if valid_row_index >= 5:
        location = 'Bottom right quadrant'
    else:
        location = 'Top right quadrant'
else:
    if valid_row_index >= 5:
        location = 'Bottom left quadrant'
    else:
        location = 'Top left quadrant'

message_name_id = f"Hello. My name is {name}. My ID is {identifier}."
message_location = f"My current location is ({valid_row_index}, {valid_column_index}). I am in the {location}"

print(message_name_id)
print(message_location)