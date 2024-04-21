import pandas as pd

def calculate_final_momentum(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df['final'] = df['momentum2'] * df['momentum1']
    df = df.drop(columns=['momentum1', 'momentum2'], errors='ignore')
    df.to_csv(output_csv, index=False)

# Example usage:
# calculate_final_momentum("aamodified_match_2023-wimbledon-1701.csv", "xaamodified_match_2023-wimbledon-1701.csv")

# import pandas as pd
# df = pd.read_csv('aamodified_match_2023-wimbledon-1701.csv')
# df['final'] = df['momentum2'] * df['momentum1']
# df.to_csv('xaamodified_match_2023-wimbledon-1701.csv')