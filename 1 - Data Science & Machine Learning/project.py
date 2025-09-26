import pandas as pd

df = pd.read_csv('../data/data.csv')


def main():

  # Print the dataframe to look for missing values or invalid data
  print('Dataframe before cleaning:')
  print(df)
  print('\n')
  
  # Drop all rows with missing values or invalid data
  df['Price_USD'] = pd.to_numeric(df['Price_USD'], errors='coerce')
  df.dropna(inplace=True)
    


  # Print the cleaned dataframe to verify the the data is clean
  print('Dataframe after cleaning:')
  print(df)
  print('\n')





if __name__ == "__main__":
  
  # Make a couple of new lines for readability and run main
  print('\n')
  main()