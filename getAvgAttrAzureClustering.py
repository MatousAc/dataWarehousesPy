import pandas as pd

fileLoc = "C:\\Users\\AcHybl\\Desktop\\code\\db\\sauAttendance\\clusteringData\\"
clusterNumber = 5

data = pd.read_csv(f"{fileLoc}cluster0{clusterNumber}AS.csv")
data = data.iloc[:, :4]
grouped = data.groupby("Assignments").mean()
print(f'grouped: ${grouped}')
print(f'grouped is ${type(grouped)}')

# data.to_csv(fileLoc + "aggregated.csv")

