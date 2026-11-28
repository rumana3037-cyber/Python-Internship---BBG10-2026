import pandas as pd

# --- Task 1: Read products.csv and display first 2 rows & shape ---
df_products = pd.read_csv("products.csv")

print("--- Task 1: First 2 Rows ---")
print(df_products.head(2))
print("\nDimensions (rows, columns):", df_products.shape)

# --- Task 2: Filter products where Price > 5000 ---
print("\n--- Task 2: Products with Price > 5000 ---")
expensive_products = df_products[df_products["Price"] > 5000]
print(expensive_products)

# --- Task 3: Read marks.csv, calculate Maths average & find topper ---
df_marks = pd.read_csv("marks.csv")

maths_avg = df_marks["Maths"].mean()
print("\n--- Task 3: Maths Analysis ---")
print("Average Maths Marks:", maths_avg)

topper_index = df_marks["Maths"].idxmax()
topper_record = df_marks.loc[topper_index]
print("\nMaths Topper Record:")
print(topper_record)