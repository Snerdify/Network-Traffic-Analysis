import pandas as pd

# Load the dataset
df = pd.read_csv('path-to-dataset')

# Check for missing values
print(df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()  # Drop rows with missing values

# If there are categorical variables, convert them to numerical format
df['categorical_column'] = pd.factorize(df['categorical_column'])[0]

# Convert timestamp column to datetime type
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract features from timestamp (e.g., hour, day, month)
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day
df['month'] = df['timestamp'].dt.month


# Convert timestamp column to datetime type
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract features from timestamp (e.g., hour, day, month)
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day
df['month'] = df['timestamp'].dt.month
