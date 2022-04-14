import pandas as pd
import statistics
import csv

df= pd.read_csv("height-weight.csv")
height_list= df["Height(Inches)"].to_list()
weight_list= df["Weight(Pounds)"].to_list()

height_mean= statistics.mean(height_list)
weight_mean= statistics.mean(weight_list)
height_median= statistics.median(height_list)
weight_median= statistics.median(weight_list)
height_mode= statistics.mode(height_list)
weight_mode= statistics.mode(weight_list)
height_std_deviation= statistics.stdev(height_list)
weight_std_deviation= statistics.stdev(weight_list)

height_1st_std_deviation_start, height_1st_std_deviation_end= height_mean-height_std_deviation, height_mean+height_std_deviation
height_2nd_std_deviation_start, height_2nd_std_deviation_end= height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
height_3rd_std_deviation_start, height_3rd_std_deviation_end= height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

weight_1st_std_deviation_start, weight_1st_std_deviation_end= weight_mean-weight_std_deviation, weight_mean+weight_std_deviation
weight_2nd_std_deviation_start, weight_2nd_std_deviation_end= weight_mean-(2*weight_std_deviation), weight_mean+(2*weight_std_deviation)
weight_3rd_std_deviation_start, weight_3rd_std_deviation_end= weight_mean-(3*weight_std_deviation), weight_mean+(3*weight_std_deviation)

height_list_of_data_within_one_std_deviation= [result for result in height_list if result>height_1st_std_deviation_start and result<height_1st_std_deviation_end]
height_list_of_data_within_two_std_deviation= [result for result in height_list if result>height_2nd_std_deviation_start and result<height_2nd_std_deviation_end]
height_list_of_data_within_three_std_deviation= [result for result in height_list if result>height_3rd_std_deviation_start and result<height_3rd_std_deviation_end]

weight_list_of_data_within_one_std_deviation= [result for result in weight_list if result>weight_1st_std_deviation_start and result<weight_1st_std_deviation_end]
weight_list_of_data_within_two_std_deviation= [result for result in weight_list if result>weight_2nd_std_deviation_start and result<weight_2nd_std_deviation_end]
weight_list_of_data_within_three_std_deviation= [result for result in weight_list if result>weight_3rd_std_deviation_start and result<weight_3rd_std_deviation_end]

print("{}% of data for height lies within one standard deviation".format(len(height_list_of_data_within_one_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within two standard deviation".format(len(height_list_of_data_within_two_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within three standard deviation".format(len(height_list_of_data_within_three_std_deviation)*100.0/len(height_list)))


print("{}% of data for weight lies within one standard deviation".format(len(weight_list_of_data_within_one_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within two standard deviation".format(len(weight_list_of_data_within_two_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within three standard deviation".format(len(weight_list_of_data_within_three_std_deviation)*100.0/len(weight_list)))

