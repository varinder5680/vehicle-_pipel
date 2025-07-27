import pandas as pd

def process_data(filepath):
    try:
        df=pd.read_csv(filepath)
        df_clean=df[(df['speed']>=0) & (df['speed']<=250)]
        df_clean= df_clean.dropna(subset=['latitude','longitude'])
        df_clean.to_csv("cleaned_vehicle_log.csv",index=False)
        print("cleaned data")
    except Exception as e:
        print(f"error: {e}")
        