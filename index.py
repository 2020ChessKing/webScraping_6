import pandas as pd, csv

#Intepret Data
df = pd.read_csv('stars_data.csv')
Distances = df["Distance"].to_list()
Gravities = df["Gravity"].to_list()

#Clean Data
def clean_data():
    Cleaned_Distances = []
    
    for i in range(len(Distances)):
        try:
            Cleaned_Distances.append(float(Distances[i]))
        except:
            float_value = float(Distances[i].replace(",", ""))
            Cleaned_Distances.append(float_value)
    
    return Cleaned_Distances

Distances = clean_data()

# Add Cleaned_Distances to CSV file
df = df.drop(["Distance"], axis=1)
df["Distance"] = Distances

df.to_csv("stars_data.csv", index=False)

data = []

# Get Data in Array Format
with open("stars_data.csv") as file:
    file_data = csv.reader(file)
    for rows in file_data:
        data.append(rows)

# Sorting Gravities
labels = data[0]
data = data[1:]

sorted_data = []

for row in data:
    Distance = float(row[4])
    Gravity = float(row[3])
    if Distance <= 100 and Gravity >= 150 and Gravity <= 350:
        sorted_data.append(row)

print(sorted_data[0])

# New CSV File
df = pd.DataFrame(columns=labels, data=sorted_data)
df.to_csv("filtered_stars.csv", index=False)