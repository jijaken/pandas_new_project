import pandas as pd

df = pd.read_csv('playstore.csv').drop(columns='Unnamed: 0')

playstore = df

data_head = playstore.head(3)
data_tail = playstore.tail(3)

n_row, n_col = playstore.shape

uniquie_app = len(set(playstore['App']))

rating_missing = playstore[playstore['Rating'].isna()].shape[0]

playstore_copy = playstore[['Category','App', 'Size','Price', 'Genres', 'Current Ver','Reviews']]
playstore_copy =  pd.concat([playstore_copy[:3], playstore_copy[5:8], playstore_copy[15:19]],sort=False)
playstore_copy.to_csv('playstore_copy.csv')

unique_playstore = playstore.drop_duplicates(subset=['App'],keep='first').reset_index(drop=True)

unique_playstore.columns = unique_playstore.columns.str.lower().str.replace(' ','_')

round((unique_playstore[unique_playstore['price']=='0'].shape[0]/ unique_playstore['price'].shape[0]),2)

education_playstore = unique_playstore[(unique_playstore['category']=='EDUCATION') & (unique_playstore['reviews']>1000)].reset_index(drop=True)

unique_playstore['price'] = unique_playstore['price'].str.replace('$','',regex=True).astype({'price':'float64'})

result = pd.pivot_table(unique_playstore, values=['price','rating','reviews'], index=['category', 'type'], aggfunc='mean')
result['price'] = round(result['price'],2)
result['rating'] = round(result['rating'],1)
result['reviews'] = round(result['reviews'],2)
result.columns = ['mean_price','mean_rating','mean_reviews']

result.to_csv('result.csv',sep=',')
