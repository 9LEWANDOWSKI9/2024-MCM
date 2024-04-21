import pandas as pd


def calculate_momentum1(input_csv, output_csv):
    data = pd.read_csv(input_csv)
    data['momentum1'] = 0
    momentum_values = []
    grouped_data_set = data.groupby('set_no')

    data.loc[data.index[0], 'momentum1'] = 5

    for group_name_set, group_data_set in grouped_data_set:
        grouped_data_game = group_data_set.groupby('game_no')
        m1 = group_data_set['p1_sets'].values
        m2 = group_data_set['p2_sets'].values
        b1 = 0

        momentum = 5

        for _, group_data_game in grouped_data_game:
            p1 = group_data_game['p1_games'].values
            p2 = group_data_game['p2_games'].values

            for j in range(1, len(p1)):
                a1 = group_data_game.loc[group_data_game.index[0], 'momentum1']

                a = p1[j] - p2[j]
                if a == 1:
                    a1 = momentum * 1.2
                elif a == 0:
                    a1 = momentum
                elif a == 2:
                    a1 = momentum * (1.2 ** 2)
                elif a == 3:
                    a1 = momentum * (1.2 ** 3)
                elif a == 4:
                    a1 = momentum * (1.2 ** 4)
                elif a == 5:
                    a1 = momentum * (1.2 ** 5)
                elif a == 6:
                    a1 = momentum * (1.2 ** 6)
                elif a == 7:
                    a1 = momentum * (1.2 ** 7)
                elif a == -1:
                    a1 = momentum / 1.2
                elif a == -2:
                    a1 = momentum / (1.2 ** 2)
                elif a == -3:
                    a1 = momentum / (1.2 ** 3)
                elif a == -4:
                    a1 = momentum / (1.2 ** 4)
                elif a == -5:
                    a1 = momentum / (1.2 ** 5)
                elif a == -6:
                    a1 = momentum / (1.2 ** 6)
                elif a == -7:
                    a1 = momentum / (1.2 ** 7)

                group_data_game.loc[group_data_game.index[0], 'momentum1'] = a1
                group_data_game.at[group_data_game.index[j], 'momentum1'] = a1
            momentum = group_data_game['momentum1'].values[-1]

            momentum_values.extend(group_data_game['momentum1'].values)

    data['momentum1'] = momentum_values
    data.to_csv(output_csv, index=False)

# Example usage:
# calculate_momentum1("modified_match_2023-wimbledon-1701.csv", "amodified_match_2023-wimbledon-1701.csv")

# import pandas as pd
#
# data = pd.read_csv("modified_match_2023-wimbledon-1701.csv")
# data['momentum1'] = 0
# momentum_values = []
# grouped_data_set = data.groupby('set_no')

# data.loc[data.index[0], 'momentum1'] = 5
#
# for group_name_set, group_data_set in grouped_data_set:
#     grouped_data_game = group_data_set.groupby('game_no')
#     m1 = group_data_set['p1_sets'].values
#     m2 = group_data_set['p2_sets'].values
#     b1 = 0
#
#     momentum = 5
#
#     for _, group_data_game in grouped_data_game:
#         p1 = group_data_game['p1_games'].values
#         p2 = group_data_game['p2_games'].values
#
#         for j in range(1, len(p1)):
#             a1 = group_data_game.loc[group_data_game.index[0], 'momentum1']
#
#             a = p1[j] - p2[j]
#             if a == 1:
#                 a1 = momentum * 1.2
#             elif a==0 :
#                 a1 = momentum
#             elif a == 2:
#                 a1 = momentum * (1.2 ** 2)
#             elif a == 3:
#                 a1 = momentum * (1.2 ** 3)
#             elif a == 4:
#                 a1 = momentum * (1.2 ** 4)
#             elif a == 5:
#                 a1 = momentum * (1.2 ** 5)
#             elif a == 6:
#                 a1 = momentum * (1.2 ** 6)
#             elif a == 7:
#                 a1 = momentum * (1.2 ** 7)
#             elif a == -1:
#                 a1 = momentum / 1.2
#             elif a == -2:
#                 a1 = momentum / (1.2 ** 2)
#             elif a == -3:
#                 a1 = momentum / (1.2 ** 3)
#             elif a == -4:
#                 a1 = momentum / (1.2 ** 4)
#             elif a == -5:
#                 a1 = momentum / (1.2 ** 5)
#             elif a == -6:
#                 a1 = momentum / (1.2 ** 6)
#             elif a == -7:
#                 a1 = momentum / (1.2 ** 7)
#
#                 # data.loc[data.index[j], 'momentum1'] = momentum
#             group_data_game.loc[group_data_game.index[0], 'momentum1'] = a1
#             group_data_game.at[group_data_game.index[j], 'momentum1'] = a1
#         momentum = group_data_game['momentum1'].values[-1]
#
#         momentum_values.extend(group_data_game['momentum1'].values)
#
# data['momentum1'] = momentum_values
# data.to_csv("amodified_match_2023-wimbledon-1701.csv", index=False)
