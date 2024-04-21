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
    grouped_data_set = data.groupby('game_no')

    momentum_values = []
    for group_name_set, group_data_set in grouped_data_set:
        point_victor_values = group_data_set['point_victor'].values

        momentum = 0
        consecutive_1_count = 0
        consecutive_2_count = 0
        for j in range(1, len(point_victor_values)):
            previous_momentum = group_data_set.at[group_data_set.index[j - 1], 'momentum']

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
            group_data_set.at[group_data_set.index[j], 'momentum'] = momentum
        momentum_values.extend(group_data_set['momentum'].values)
    data['momentum'] = momentum_values

    data.to_csv(output_csv, index=False)

