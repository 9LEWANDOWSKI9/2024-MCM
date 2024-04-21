import pandas as pd

def calculate_momentum(input_csv, output_csv):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    data = pd.read_csv(input_csv)
    data['momentum'] = 0

    momentum_values = []

    grouped_data_set = data.groupby('set_no')

    for group_name_set, group_data_set in grouped_data_set:
        grouped_data_game = group_data_set.groupby('game_no')
        for group_name_game, group_data_game in grouped_data_game:
            group_data_game.loc[group_data_game.index[0], 'momentum'] = 1
            point_victor_values = group_data_game['point_victor'].values

            momentum = 0
            consecutive_1_count = 0
            consecutive_2_count = 0

            for j in range(1, len(point_victor_values)):
                previous_momentum = group_data_game.at[group_data_game.index[j - 1], 'momentum']

                if point_victor_values[j - 1] == 1:
                    consecutive_1_count += 1
                    consecutive_2_count = 0
                elif point_victor_values[j - 1] == 2:
                    consecutive_2_count += 1
                    consecutive_1_count = 0
                else:
                    consecutive_1_count = 0
                    consecutive_2_count = 0

                if consecutive_1_count >= 1:
                    momentum += fibonacci(consecutive_1_count)
                elif consecutive_2_count >= 1:
                    momentum -= fibonacci(consecutive_2_count)

                # if group_data_game['p1_ace'].values[j - 1] == 1:
                #     momentum += 2.5
                #
                # if group_data_game['p1_double_fault'].values[j - 1] == 1:
                #     momentum -= 1.7
                #
                # if group_data_game['p1_unf_err'].values[j - 1] == 1:
                #     momentum -= 0.8

                group_data_game.at[group_data_game.index[j], 'momentum'] = momentum


            momentum_values.extend(group_data_game['momentum'].values)


    data['momentum'] = momentum_values


    data.to_csv(output_csv, index=False)

# Example usage:
# calculate_momentum("match_2023-wimbledon-1701.csv", "modified_match_2023-wimbledon-1701.csv")

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b
# import pandas as pd
#

# data = pd.read_csv("match_2023-wimbledon-1701.csv")
# data['momentum'] = 0
#
# momentum_values = []
#
# grouped_data_set = data.groupby('set_no')

# for group_name_set, group_data_set in grouped_data_set:
#     grouped_data_game = group_data_set.groupby('game_no')
#     for group_name_game, group_data_game in grouped_data_game:
#         group_data_game.loc[group_data_game.index[0], 'momentum'] = 1
#         point_victor_values = group_data_game['point_victor'].values
#
#         momentum = 0
#         consecutive_1_count = 0
#         consecutive_2_count = 0
#
#         for j in range(1, len(point_victor_values)):
#             previous_momentum = group_data_game.at[group_data_game.index[j - 1], 'momentum']
#
#             if point_victor_values[j - 1] == 1:
#                 consecutive_1_count += 1
#                 consecutive_2_count = 0
#             elif point_victor_values[j - 1] == 2:
#                 consecutive_2_count += 1
#                 consecutive_1_count = 0
#             else:
#                 consecutive_1_count = 0
#                 consecutive_2_count = 0
#
#
#             if consecutive_1_count >= 1:
#                 momentum += fibonacci(consecutive_1_count)
#             elif consecutive_2_count >= 1:
#                 momentum -= fibonacci(consecutive_2_count)
#
#             if group_data_game['p1_ace'].values[j - 1] == 1:
#                 momentum += 2.5
#
#             if group_data_game['p1_double_fault'].values[j - 1] == 1:
#                 momentum -= 1.7
#
#             if group_data_game['p1_unf_err'].values[j - 1] == 1:
#                 momentum -= 0.8
#
#             group_data_game.at[group_data_game.index[j], 'momentum'] = momentum
#
#
#         momentum_values.extend(group_data_game['momentum'].values)

# data['momentum'] = momentum_values

# data.to_csv("modified_match_2023-wimbledon-1701.csv", index=False)
#
