import pandas as pd

fileLoc = "C:\\Users\\AcHybl\\Desktop\\code\\db\\db&dw\\usgsEarthquakes\\"
data =  pd.DataFrame()

for year in range(1990, 2022):
  print(f"\n{year}", end=' ')
  for month in range(1, 13):
    print(f"{month}", end=' ')
    if (year == 2021 and month > 8): continue
    df = pd.read_csv(f"{fileLoc}{year}_{month}.csv")
    df["year"] = year
    df["month"] = month
    data = pd.concat([data, df])

data.to_csv(fileLoc + "aggregated.csv")


