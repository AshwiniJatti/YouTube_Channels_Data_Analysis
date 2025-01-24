import pandas as pd

#Reading file from the folder
data = pd.read_csv("C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_1M_clean.csv")

#Creating a separate dataset for country India
data_india = data[data['country'] == 'India']

#Dropping null values from the dataset
filtered_data_india = data_india.dropna()

#filtering data based of description value 'food'
filtered_data_india_food = filtered_data_india.loc[filtered_data_india['keywords'].str.contains('food|cook|cooking')]

print(len(filtered_data_india_food))

#Writing a dataframe to the csv file
filtered_data_india_food.to_csv('C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_india_food.csv')