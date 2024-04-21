# from tetstt import calculate_momentum1
# from dataa import calculate_momentum
# from tennis import calculate_momentum2
# from mul import calculate_final_momentum
# input_csv = "match_2023-wimbledon-1301.csv"
# output_csv = "match_2023-wimbledon-1301.csv"
# calculate_momentum(input_csv, output_csv)
# calculate_momentum1(input_csv, output_csv)
# calculate_momentum2(input_csv, output_csv)
# calculate_final_momentum(input_csv, output_csv)

from tetstt import calculate_momentum1
from dataa import calculate_momentum
from tennis import calculate_momentum2
from mul import calculate_final_momentum
from WYH import calculate_momentum
file_pattern = "ping.csv"

input_csv = file_pattern

calculate_momentum(input_csv, input_csv)
# calculate_momentum1(input_csv, input_csv)
calculate_momentum2(input_csv, input_csv)
# calculate_final_momentum(input_csv, input_csv)
