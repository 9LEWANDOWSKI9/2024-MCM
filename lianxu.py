def count_all_consecutive_occurrences(lst, target_element):
    counts = []
    count = 0

    for element in lst:
        if element == target_element:
            count += 1
        else:
            if count > 0:
                counts.append(count)
            count = 0

    if count > 0:
        counts.append(count)

    return counts

my_list = [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
target_element = 1

result = count_all_consecutive_occurrences(my_list, target_element)
print(f"All consecutive occurrences of {target_element}: {result}")
# if (j + 1) < len(consecutive_values) and consecutive_values[j] == 1 and consecutive_values[j + 1] != 1:
#     momentum += 1
# elif (j + 2) < len(consecutive_values) and consecutive_values[j] == 1 and consecutive_values[j + 1] == 1 and \
#         consecutive_values[j + 2] != 1:
#     momentum += 1
# elif (j + 3) < len(consecutive_values) and consecutive_values[j] == 1 and consecutive_values[j + 1] == 1 and \
#         consecutive_values[j + 2] == 1 and consecutive_values[j + 3] != 1:
#     momentum += 2
# elif (j + 4) < len(consecutive_values) and consecutive_values[j] == 1 and consecutive_values[j + 1] == 1 and \
#         consecutive_values[j + 2] == 1 and consecutive_values[j + 3] == 1 and consecutive_values[j + 4] != 1:
#     momentum += 3
# elif (j + 5) < len(consecutive_values) and consecutive_values[j] == 1 and consecutive_values[j + 1] == 1 and \
#         consecutive_values[j + 2] == 1 and consecutive_values[j + 3] == 1 and consecutive_values[j + 4] == 1 and \
#         consecutive_values[j + 5] != 1:
#     momentum += 5
# elif (j + 6) < len(consecutive_values) and consecutive_values[j] == 1 and consecutive_values[j + 1] == 1 and \
#         consecutive_values[j + 2] == 1 and consecutive_values[j + 3] == 1 and consecutive_values[j + 4] == 1 and \
#         consecutive_values[j + 5] == 1 and consecutive_values[j + 6] != 1:
#     momentum += 8
# elif (j + 1) < len(consecutive_values) and consecutive_values[j] == 2 and consecutive_values[j + 1] != 2:
#     momentum -= 1
# elif (j + 2) < len(consecutive_values) and consecutive_values[j] == 2 and consecutive_values[j + 1] == 2 and \
#         consecutive_values[j + 2] != 2:
#     momentum -= 1
# elif (j + 3) < len(consecutive_values) and consecutive_values[j] == 2 and consecutive_values[j + 1] == 2 and \
#         consecutive_values[j + 2] == 2 and consecutive_values[j + 3] != 2:
#     momentum -= 2
# elif (j + 4) < len(consecutive_values) and consecutive_values[j] == 2 and consecutive_values[j + 1] == 2 and \
#         consecutive_values[j + 2] == 2 and consecutive_values[j + 3] == 2 and consecutive_values[j + 4] != 2:
#     momentum -= 3
# elif (j + 5) < len(consecutive_values) and consecutive_values[j] == 2 and consecutive_values[j + 1] == 2 and \
#         consecutive_values[j + 2] == 2 and consecutive_values[j + 3] == 2 and consecutive_values[j + 4] == 2 and \
#         consecutive_values[j + 5] != 2:
#     momentum -= 5
# elif (j + 6) < len(consecutive_values) and consecutive_values[j] == 2 and consecutive_values[j + 1] == 2 and \
#         consecutive_values[j + 2] == 2 and consecutive_values[j + 3] == 2 and consecutive_values[j + 4] == 2 and \
#         consecutive_values[j + 5] == 2 and consecutive_values[j + 6] != 2:
#     momentum -= 8