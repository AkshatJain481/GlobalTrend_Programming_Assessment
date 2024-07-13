import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def clean_and_preprocess(df):
    # Handling missing values
    # Numerical columns: Impute missing values with mean
    numerical_cols = ['A', 'B']  # Specify the numerical columns/attributes

    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

    # Categorical columns: Impute missing values with mode
    categorical_cols = ['C']  # Specify the categorical column/attributes
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

    # Normalizing numerical columns using Min-Max scaling
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df

# Step 1: Read the CSV file into a DataFrame
file_path = 'sample_dataset.csv'
df = pd.read_csv(file_path)

# Step 2: Clean and preprocess the DataFrame for columns A, B, and C
df = clean_and_preprocess(df)

# Step 3: Save the updated DataFrame back to the CSV file, overwriting it
df.to_csv(file_path, index=False)

print(f"Updated dataset saved to {file_path}")
