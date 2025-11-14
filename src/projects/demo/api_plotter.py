# This python program pull the last 24h of Bitcoin prices (USD) from CoinGecko, plot price vs time, and saves files.
from pathlib import Path
import argparse
import requests
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_NAME = "api_plotter"
DEFAULT_OUT = Path(f"data/projects/{PROJECT_NAME}")
OPEN_METEO = "https://api.open-meteo.com/v1/forecast?latitude=35.68&longitude=139.69&hourly=temperature_2m"

# to fetch JSON from URL
def fetch_json(url: str) -> dict:
    # send HTTP GET request to the URL and wait up to 20s           
    r = requests.get(url, timeout = 20)     

    # If the request fails (e.g., 404 or 500 error), this line will raise an exception
    r.raise_for_status()    

    return r.json()

# to convert the fetched data (json) to dataframe
def to_dataframe(payload: dict) -> pd.DataFrame:
    # get the list from payload [hourly list] and [temperature list]
    hourly = payload["hourly"]

    #construct dataframe from the API with column names
    df = pd.DataFrame({"time": hourly["time"], "temperature": hourly["temperature_2m"]})

    # convert the info of time to date time format
    df["time"] = pd.to_datetime(df["time"])
    df = df.sort_values("time").dropna().reset_index(drop = True)

    return df

# to plot the data
def plot_series(df: pd.DataFrame, plot_dir: Path) -> Path:      
    # create a folder if does not exist       
    plot_dir.mkdir(parents = True, exist_ok = True)   

    # prepare the canvas
    plt.figure(figsize = (8, 4))      

    # plot the followings:
        # x = time (ms)
        # y = price (USD)
        # line label = f"{coin.upper()} price ({fiat.upper()})"
    plt.plot(df["time"], df["temperature"], color = "orange", label = "Temperature (C)") 

    # title for the plot
    plt.title("Tokyo 24-Hour Temperature Trend")                                       
    
    # x label
    plt.xlabel("Time")       

    # y label
    plt.ylabel("Temperature (°C)")     

    # Rotate time labels by 30 degrees for better readability                                          
    plt.xticks(rotation = 30, ha="right")

    # grid on                                               
    plt.grid(True)   

    # label for the represented line                                                                   
    plt.legend()      

    # Automatically adjust spacing so labels/titles don’t overlap                                                                  
    plt.tight_layout()    
    
    # define thhe pathh for the file output                                                             
    out_png = plot_dir / "tokyo_temperature_24h.png"    

    #save and close thhe image                                  
    plt.savefig(out_png)
    plt.close()                                                                         
    return out_png                                                                      

# to create and save csv (comma separated values) file
def save_csv(df: pd.DataFrame, csv_dir: Path) -> Path:
    # create a folder if not exist
    csv_dir.mkdir(parents=True, exist_ok=True)  

    # create csv file named f"{coin}_{fiat}_24h.csv"                                                      
    out_csv = csv_dir / "tokyo_temperature_24h.csv"   

    # index=False removes the numeric row index (0,1,2,…) from the file                                         
    df.to_csv(out_csv, index = False)                                                  
    return out_csv

# # to get arguments from terminal 
# def get_args():
#     p = argparse.ArgumentParser(description="API -> DataFrame -> Plot")                                 # parse data from arguments entered in the terminal
#     p.add_argument("--coin", default = "bitcoin", help = "CoinGecko coin id (e.g. bitcoin, ethereum)")  # get argument "--coin", specify which crypto 
#     p.add_argument("--fiat", default = "usd", help = "Fiat currency (usd, eur, jpy)")                   # get argument "--fiat", specify whhich currency
#     p.add_argument("--out", type = Path, default=DEFAULT_OUT, help="Output directory")                 # get argument "--out", specify which directory/folder to save the output files in 
#     return p.parse_args()                                                                               # return te collected argument


def main(): 
    # fetching
    url = OPEN_METEO
    payload = fetch_json(url)
    df = to_dataframe(payload)

    #
    plot_dir = DEFAULT_OUT / "plot"
    csv_dir = DEFAULT_OUT / "csv"

    # save outputs
    png_path = plot_series(df, plot_dir)
    csv_path = save_csv(df, csv_dir)
    print("Saved", csv_path, "and", png_path)


if __name__ == "__main__":
    main()