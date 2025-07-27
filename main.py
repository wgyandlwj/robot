import hashlib

grid_zie = 10

name = input("What is the name of the robot?")
identifier = hashlib.sha256(name.encode()).hexdigest()

row_index = int(input("Enter current row index: "))
column_index = int(input("Enter current column index: "))

initial_direction = input("What is its initial direction [n|s|e|w]?")

valid_row_index = max(min(row_index, grid_zie - 1), 0)
valid_column_index = max(min(column_index, grid_zie - 1), 0)

if valid_row_index <= 4:
    location_part_1 = 'top'
else:
    location_part_1 = 'bottom'

if valid_column_index > 4:
    location_part_2 = 'right'
else:
    location_part_2 = 'left'



if initial_direction == 'n':
    facing = 'North'
    next_row_index = valid_row_index + 1
    next_column_index = valid_column_index

elif initial_direction == 'e':
    facing = 'East'
    next_column_index = valid_column_index + 1
    next_row_index = valid_row_index
elif initial_direction == 'w':
    facing = 'West'
    next_column_index = valid_column_index - 1
    next_row_index = valid_row_index
else:
    facing = 'South'
    next_row_index = valid_row_index - 1
    next_column_index = valid_column_index

next_row_index =  max(min(next_row_index, grid_zie - 1), 0)
next_column_index = max(min(next_column_index, grid_zie - 1), 0)

if next_row_index <= 4:
    location_part_3 = 'top'
else:
    location_part_3 = 'bottom'

if next_column_index > 4:
    location_part_4 = 'right'
else:
    location_part_4 = 'left'

message_name_id = f"Hello. My name is {name}. My ID is {identifier}."
message_location = f"My current location is ({valid_row_index}, {valid_column_index}). I am in the {location_part_1} {location_part_2} quadrant."
message_facing = f"I am facing {facing}."
message_location_2 = f"My current location is ({next_row_index}, {next_column_index}). I am in the {location_part_3} {location_part_4} quadrant."

print(message_name_id)
print(message_location)
print(message_facing)
print("Moving one step forward.")
print(message_location_2)


