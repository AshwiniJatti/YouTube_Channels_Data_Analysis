import pandas as pd

#Reading file from the folder
data = pd.read_csv("C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_channels_1M_clean.csv")

# Dropping columns which are not required for the analysis
#errors = 'ignore' ignores the errors if columns are not present in the dataset
data = data.drop(['banner_link','description','avatar'], axis=1, errors='ignore')

#Dropping null values for the selected columns
filtered_data = data.dropna(subset = ['country','channel_name','total_views','subscriber_count','total_videos','join_date'])
len(filtered_data)

#changing the datatype to datetime format
filtered_data['join_date'] = pd.to_datetime(filtered_data['join_date'])

#Fetching year from the join date column
filtered_data['start_year'] = filtered_data['join_date'].dt.year

#Writing a dataframe to the csv file
filtered_data.to_csv('C:/Ashwini/Hobby Project/2024YTChannels/Data/youtube_filtered_data.csv')


