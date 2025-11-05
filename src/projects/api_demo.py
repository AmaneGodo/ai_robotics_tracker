# 1. import the necessary modules
from pathlib import Path
import argparse
import json

import requests
import pandas as pd
import matplotlib.pyplot as plt

# 2. pick an API and prototype the URL
    # isolate URLL building in a function so it's easy to swap APIs later
    # does not fetch info yet, first we construct/inspect the URL
def build_url(lat: float, lon: float) -> str:
    base="https://api.open-meteo.com/v1/forecast"

    #request hourly temperatures; timezone=auto simplifies timestamps
    return (
        f"{base}?latitude={lat}&longitude={lon}"
        "&hourly=temperature_2m"
        "&forecast_days=2"
        "&timezone=auto"
    )

# 3. fetch wit timeouts + error handling
    # fetching json but not parsing
def fetch_json(url: str) -> dict:
    resp = requests.get(url, timeout = 20)
    resp.raise_for_status()  # 4xx/5xx -> exception with clear message
    return resp.json()

# 4. parse JSON -> DataFrame
def to_dataframe(payload: dict, hours: int) -> pd.DataFrame:
    # defensive lookups; crash with a helpful KeyError if schema changes
    hours_block = payload["hourly"]
    times = pd.to_datetime(hours_block["time"])
    temps = hours_block["temperature_2m"]
    df = pd.DataFrame({"time":times, "temp_c":temps}).sort_values("time")
    return df.head(hours)

# 5. file outputs(save csv + raw json)
def save_outputs(df: pd.DataFrame, raw: dict, out_dir: Path) -> None: #return None because saving is a side effect of thhe function
    out_dir.mkdir(exist_ok=True)
    (out_dir / "weather_hourly.csv").write_text(df.to_csv(index=False))
    (out_dir / "raw_response.json").write_text(json.dumps(raw, indent=2))

# 6. make a simple plot (no style fuss)
    # make it pretty later
def plot_temperature(df: pd.DataFrame, out_dir: Path):
    plt.figure()
    plt.plot(df["time"], df["temp_c"])
    plt.title("Hourly Temperature (°C)")
    plt.xlabel("time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    out_path = out_dir / "temperature_plot.png"
    plt.savefig(out_path)
    plt.close()
    return out_path

# 7. CLI arguments (the user interface)
    # this push all I/O to main(). This keeps function reusabble in other scripts
def get_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="API → JSON → DataFrame → Plot demo (Open-Meteo)")
    p.add_argument("--lat", type=float, default=35.78, help="Latitude (default: Raleigh, NC)")
    p.add_argument("--lon", type=float, default=-78.64, help="Longitude (default: Raleigh, NC)")
    p.add_argument("--hours", type=int, default=24, help="How many upcoming hours to show")
    p.add_argument("--out", type=Path, default=Path("data/projects/api_demo"), help="Output directory")
    return p.parse_args()

# 8. Wire it toggether (composition)
    # keep main() linear and readable; eachh step calls the function above
def main():
    args = get_args()
    url = build_url(args.lat, args.lon)
    raw = fetch_json(url)
    df = to_dataframe(raw, hours=args.hours)
    save_outputs(df, raw, args.out)
    plot_path = plot_temperature(df, args.out)
    print("✅ saved:", args.out / "weather_hourly.csv", "and", plot_path)

# 9. The safe entry point
if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        print(f"❌ error: {e}")
        raise