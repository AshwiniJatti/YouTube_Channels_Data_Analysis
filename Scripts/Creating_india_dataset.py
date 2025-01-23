import pandas as pd

#Reading file from the folder
data = pd.read_csv("C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_1M_clean.csv")

#Creating a separate dataset for country India
data_india = data[data['country'] == 'India']

#Writing a dataframe to the csv file
data_india.to_csv('C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_india.csv')


