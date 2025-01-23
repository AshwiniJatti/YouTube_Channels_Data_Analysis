import pandas as pd

# Reading dataset
data = pd.read_csv("C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_1M_clean.csv")

#print(data.head())
print(len(data))
print(data.shape)
print(len(data.columns))

#Removing duplicates
data_cleaned = data.drop_duplicates()
print(len(data_cleaned))

print(data.columns)


