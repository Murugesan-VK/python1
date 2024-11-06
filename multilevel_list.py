multilevel_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(multilevel_list[2])  # Output: [7, 8, 9]
print(multilevel_list[1][1])  # Output: 5

del multilevel_list[1]
print(multilevel_list)      # Output: [[1, 2, 3], [7, 8, 9]]
