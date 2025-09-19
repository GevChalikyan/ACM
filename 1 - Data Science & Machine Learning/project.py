import pandas as pd

df = pd.read_csv("../data/data.csv")


def main():
  
  if df['Num_Bedrooms'].isnull().any():
    df.dropna(subset=['Num_Bedrooms'], inplace=True)



  mask = df['Price_USD'].apply(lambda x: isinstance(x, str))
  df.loc[mask, 'Price_USD'] = df.loc[mask, 'Price_USD'].str.replace('$', '')
  df.loc[mask, 'Price_USD'] = df.loc[mask, 'Price_USD'].str.replace(',', '')

  df['Price_USD'] = pd.to_numeric(df['Price_USD'], errors='coerce')



  if df['Price_USD'].isnull().any():
    mean_price = df['Price_USD'].mean() 
    df['Price_USD'] = df['Price_USD'].fillna(mean_price)
    


  print(df)





if __name__ == "__main__":
  main()