import pandas as pd

#Reading file from the folder
data = pd.read_csv("C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_1M_clean.csv")

#Dropping null values from the dataset
filtered_data = data.dropna()

#filtering data based of description value 'food'
filtered_data_food = filtered_data.loc[filtered_data['keywords'].str.contains('food|cook|cooking')]

#filtering data where the subscriber count is greater than equal to 1M
filtered_data_food_1M = filtered_data_food[filtered_data_food['subscriber_count'] >= 1000000]

print(len(filtered_data_food))
print(len(filtered_data_food_1M))

#Writing a dataframe to the csv file
filtered_data_food_1M.to_csv('C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_food.csv')