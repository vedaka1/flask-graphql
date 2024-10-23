# for new_coord in new_coords:
#     new_coord_str += str(
#         f'{Formatter(new_coord.latitude).format_float_to_round_coords}, '
#         + f'{Formatter(new_coord.longitude).format_float_to_round_coords}
#         +{f", {new_coord.altitude}" if new_coord.altitude else ""}; \n'
#     )

# for old_coord in old_coords:
#     old_coord_str += f'{Formatter(old_coord.latitude).format_float_to_round_coords}, {Formatter(old_coord.longitude).format_float_to_round_coords}{f", {old_coord.altitude}" if old_coord.altitude else ""}; \n'

test = 123
old_coord_str = ""
new_coord_str = ""
latitude = 12.14
longitude = 16.21
altitude = f", {test}" if test else ""

new_coord_str += f"{latitude}, {longitude}{altitude}; \n"
old_coord_str += f'{latitude}, {longitude}{f", {test}" if test else ""}; \n'

print(new_coord_str)
print(old_coord_str)
