import numpy as np
import pandas as pd
import sys
import textwrap

MAX_ARG = 8

def print_arr(arr:np.array, name:str="", dim:int=1, leading_tabs:int=0):

  tabs = '\t' * leading_tabs

  if name:
    print(f"{tabs}{name}:\n")

  if dim == 1:
    print(f"{tabs}\t{arr}\n")

  elif dim == 2:
    print(f"{tabs}\t[")
    for row in arr:
      print(f"{tabs}\t\t{row}")
    print(f"{tabs}\t]\n")

def print_df(df:pd.DataFrame, name:str="", leading_tabs:int=0):

  tabs = '\t' * leading_tabs

  if name:
    print(f"{tabs}{name}:\n")

  tab_separated_string = df.to_string()
  indented_string = textwrap.indent(tab_separated_string, prefix=tabs + '\t')
  print(f"{indented_string}\n")




















def main(arg:int = 0):
    
  # SECTION 1 START
  # 1. Numpy Arrays
  if arg == 1 or arg == 0:

    # Create a Numpy array from a list of integers
    arr = np.array([1, 2, 3, 4, 5, 6])
  # SECTION 1 END





  # SECTION 2 START
  # 2. Numpy Matrices
  if arg == 2 or arg == 0:

    # Create a 2D Numpy array from a list of lists
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
  # SECTION 2 END





  # SECTION 3 START
  # 3. Numpy Indexing and Slicing
  if arg == 3 or arg == 0:

    # Create a Numpy array and a Numpy matrix
    arr = np.array([1, 2, 3, 4, 5, 6])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    # Accessing elements in a Numpy array
    first_element = arr[0]
    last_element = arr[-1]

    # Slicing a Numpy array
    sub_array = arr[1:5]
    first_two_elements = arr[:2]
    every_second_element_in_range = arr[1:5:2]
    every_second_element = arr[::2]
    reversed_array = arr[::-1]
    last_column = matrix[:, -1]
  # SECTION 3 END
    




  # SECTION 4 START
  # 4. Numpy Random Data
  if arg == 4 or arg == 0:

    # Generate a random Numpy array with 3 elements
    random_arr = np.random.rand(3)

    # Generate a random Numpy matrix with 3 rows and 2 columns
    random_matrix = np.random.rand(3, 2)
  # SECTION 4 END





  # SECTION 5 START
  # 5. Numpy Operations
  if arg == 5 or arg == 0:

    # Create two Numpy arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    # Element-wise addition
    sum_arr = arr1 + arr2

    # Element-wise multiplication
    product_arr = arr1 * arr2

    # Sum of Elements
    sum_of_elements = np.sum(arr1)

    # Dot product
    dot_product = np.dot(arr1, arr2)

    # Mean of an array
    mean_value = np.mean(arr1)

    # Standard deviation of an array
    std_dev = np.std(arr1)
  # SECTION 5 END





  # SECTION 6 START
  # 6. Numpy Constants and Mathematical Functions
  if arg == 6 or arg == 0:
    
    # Mathematical constants
    pi = np.pi
    e = np.e

    # Mathematical functions
    x = 5
    y = 3
    slope = np.tan(y / x)
    angle = np.arctan(slope)
    angle_degrees = np.degrees(angle)
  # SECTION 6 END





  # SECTION 7 START
  # 7. Pandas DataFrames
  if arg == 7 or arg == 0:
    
    # Create a Pandas DataFrame from a dictionary
    data = {
      "calories": [420, 380, 390],
      "duration": [50, 40, 45]
    }

    dictionary_df = pd.DataFrame(data)

    # Create a Pandas DataFrame by reading a CSV file
    csv_df = pd.read_csv("../data/data.csv")
    # csv_df = pd.read_excel("../data/data.xlsx")
  # SECTION 7 END





  # SECTION 8 START
  # 8. Pandas Data Cleaning and Manipulation
  if arg == 8 or arg == 0:
    
    # Create a Pandas DataFrame from a dictionary
    data = {
      "calories": [420, np.NaN, 390, 380],
      "duration": [50, 40, 45, "30 minutes"]
    }
    original_df = pd.DataFrame(data)

    # Handling Missing Data
    # a) Drop rows with NaN values in the 'calories' column
    if original_df["calories"].isnull().any():
      not_nan_df = original_df.dropna(subset=["calories"])

    # b) Fill NaN values in the 'calories' column with mean of the column
    filled_df = original_df.fillna(original_df["calories"].mean())
    
    # Handling incorrect data types
    un_strung_df = filled_df.copy()
    mask = un_strung_df["duration"].apply(lambda x: isinstance(x, str))
    un_strung_df.loc[mask, "duration"] = un_strung_df.loc[mask, "duration"].str.replace(" minutes", "")
    un_strung_df["duration"] = pd.to_numeric(un_strung_df["duration"], errors="coerce")

    # Normalizing Data
    normalized_df = un_strung_df.copy()
    normalized_df["calories"] = (normalized_df["calories"] - normalized_df["calories"].min()) / (normalized_df["calories"].max() - normalized_df["calories"].min())
    normalized_df["duration"] = (normalized_df["duration"] - normalized_df["duration"].min()) / (normalized_df["duration"].max() - normalized_df["duration"].min())
  # SECTION 8 END





  # N. Print Statements
  # PRINT 1 START
  def print_1():
    print_arr(arr, "1) Numpy Array")
  # PRINT 1 END
  # PRINT 2 START
  def print_2():
    print_arr(matrix, "2) Numpy Matrix", dim=2)
  # PRINT 2 END
  # PRINT 3 START
  def print_3():
    print_arr(arr, "3) Numpy Indexing and Slicing")
    print(f"\tFirst Element: {first_element}")
    print(f"\tLast Element: {last_element}\n")
    print(f"\tSub-array (indices 1 to 4): {sub_array}")
    print(f"\tFirst two elements: {first_two_elements}")
    print(f"\tEvery second element (indices 1 to 4): {every_second_element_in_range}")
    print(f"\tEvery second element: {every_second_element}")
    print(f"\tReversed array: {reversed_array}\n")
    print_arr(matrix, dim=2)
    print(f"\tLast column of matrix: {last_column}\n")
  # PRINT 3 END
  # PRINT 4 START
  def print_4():
    print("4) Numpy Random Data:\n")
    print_arr(random_arr, "a) Random Array", leading_tabs=1)
    print_arr(random_matrix, "b) Random Matrix", dim=2, leading_tabs=1)
  # PRINT 4 END
  # PRINT 5 START
  def print_5():
    print("5) Numpy Operations:\n")
    print_arr(arr1, "Array 1", leading_tabs=1)
    print_arr(arr2, "Array 2", leading_tabs=1)
    print_arr(sum_arr, "a) Element-wise Addition", leading_tabs=1)
    print_arr(product_arr, "b) Element-wise Multiplication", leading_tabs=1)
    print(f"\tSum of Elements in Array 1: {sum_of_elements}\n")
    print(f"\tc) Dot Product: {dot_product}\n")
    print(f"\td) Mean of Array 1: {mean_value}\n")
    print(f"\te) Standard Deviation of Array 1: {std_dev}\n")
  # PRINT 5 END
  # PRINT 6 START
  def print_6():
    print("6) Numpy Constants and Mathematical Functions:\n")
    print(f"\tMathematical Constants:")
    print(f"\t\tPi: {pi}")
    print(f"\t\tEuler's Number (e): {e}\n")
    print(f"\tMathematical Functions:")
    print(f"\t\tFor x = {x} and y = {y}:")
    print(f"\t\tSlope (tan(y/x)): {slope}")
    print(f"\t\tAngle (arctan(slope)): {angle} radians")
    print(f"\t\tAngle in Degrees: {angle_degrees}°\n")
  # PRINT 6 END
  # PRINT 7 START
  def print_7():
    print("7) Pandas DataFrames:\n")
    print_df(dictionary_df, "a) DataFrame from Dictionary", leading_tabs=1)
    print_df(csv_df, "b) DataFrame from CSV File", leading_tabs=1)
  # PRINT 7 END
  # PRINT 8 START
  def print_8():
    print("8) Pandas Data Cleaning and Manipulation:\n")
    print_df(original_df, "Original DataFrame", leading_tabs=1)
    print_df(not_nan_df, "a) DataFrame after Dropping NaN Values", leading_tabs=1)
    print_df(filled_df, "b) DataFrame after Filling NaN Values with mean", leading_tabs=1)
    print_df(un_strung_df, "c) DataFrame after Converting 'duration' to Numeric", leading_tabs=1)
    print_df(normalized_df, "d) Normalized DataFrame", leading_tabs=1)
  # PRINT 8 END

  match arg:

    case 1:
      print_1()

    case 2:
      print_2()

    case 3:
      print_3()

    case 4:
      print_4()

    case 5:
      print_5()

    case 6:
      print_6()

    case 7:
      print_7()

    case 8:
      print_8()

    case _:
      print_1()
      print_2()
      print_3()
      print_4()
      print_5()
      print_6()
      print_7()
      print_8()








if __name__ == "__main__":
  if sys.argv.__len__() > 1:
    try:
      for arg in sys.argv[1:]:
        arg = int(arg)
        if arg < 0 or arg > MAX_ARG:
          print(f"Invalid argument. Please provide an integer between 0 and {MAX_ARG}.")
        else:
          main(arg)
    except ValueError:
      print(f"Invalid argument. Please provide an integer between 0 and {MAX_ARG}.")
  else:
    main()