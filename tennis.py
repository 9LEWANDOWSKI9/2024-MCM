import pandas as pd

def calculate_momentum2(input_csv, output_csv):
    data = pd.read_csv(input_csv)
    data['momentum2'] = 0
    momentum_values = []
    grouped_data_set = data.groupby('game_no')
    data.loc[data.index[0], 'momentum2'] = 1

    for group_name_set, group_data_set in grouped_data_set:
        m1 = group_data_set['p1_games'].values
        m2 = group_data_set['p2_games'].values
        momentum = 1

        for i in range(1, len(m1)):
            b1 = group_data_set.loc[group_data_set.index[0], 'momentum2']
            b = m1[i] - m2[i]

            if b == 0:
                b1 = momentum
            elif b == 1:
                b1 = momentum * 1.5
            elif b == 2:
                b1 = momentum * (1.5 ** 2)
            elif b == 3:
                b1 = momentum * (1.5 ** 3)
            elif b == -1:
                b1 = momentum / 1.5
            elif b == -2:
                b1 = momentum / (1.5 ** 2)
            elif b == -3:
                b1 = momentum / (1.5 ** 3)

            group_data_set.loc[group_data_set.index[0], 'momentum2'] = b1
            group_data_set.at[group_data_set.index[i], 'momentum2'] = b1

        momentum = group_data_set['momentum2'].values[-1]
        momentum_values.extend(group_data_set['momentum2'].values)

    data['momentum2'] = momentum_values
    data.to_csv(output_csv, index=False)

# Example usage:
# calculate_momentum2("amodified_match_2023-wimbledon-1701.csv", "aamodified_match_2023-wimbledon-1701.csv")

# import pandas as pd
#
# data = pd.read_csv("amodified_match_2023-wimbledon-1701.csv")
# data['momentum2'] = 0
# momentum_values = []
# grouped_data_set = data.groupby('set_no')
# data.loc[data.index[0], 'momentum2'] = 1
# for group_name_set, group_data_set in grouped_data_set:
#     # print(group_data_set)
#     m1 = group_data_set['p1_sets'].values
#     m2 = group_data_set['p2_sets'].values
#     momentum = 1
#     for i in range(1, len(m1)):
#         b1 = group_data_set.loc[group_data_set.index[0], 'momentum2']
#         b = m1[i] - m2[i]
#         if b == 0:
#             b1 = momentum
#         elif b == 1:
#             b1 = momentum * 1.5
#         elif b == 2:
#             b1 = momentum * (1.5 ** 2)
#         elif b == 3:
#             b1 = momentum * (1.5 ** 3)
#         elif b == -1:
#             b1 = momentum / 1.5
#         elif b == -2:
#             b1 = momentum / (1.5 ** 2)
#         elif b == -3:
#             b1 = momentum / (1.5 ** 3)
#         group_data_set.loc[group_data_set.index[0], 'momentum2'] = b1
#         group_data_set.at[group_data_set.index[i], 'momentum2'] = b1
#     momentum = group_data_set['momentum2'].values[-1]
#
#     momentum_values.extend(group_data_set['momentum2'].values)
#
# data['momentum2'] = momentum_values
# data.to_csv("aamodified_match_2023-wimbledon-1701.csv", index=False)