import argparse
from pathlib import Path
from .data_handler import build_url, fetch_json, to_dataframe
from .plot_util import plot_single, plot_multi

PROJECT_NAME = "api_plotter"
DEFAULT_OUT = Path(f"data/projects/{PROJECT_NAME}")

def get_args():
    p = argparse.ArgumentParser(description="Open-Meteo plotter")
    p.add_argument("--lat", type=float, default=42.36, help="Latitude")
    p.add_argument("--lon", type=float, default=-71.06, help="Longitude")
    p.add_argument("--vars", nargs="+", default=["temperature_2m"], help="Variables to fetch")
    p.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output folder")
    return p.parse_args()

def main():
    args = get_args()

    url = build_url(args.lat, args.lon, args.vars)
    print("Fetching:", url)
    payload = fetch_json(url)

    df = to_dataframe(payload, args.vars)

    csv_dir = args.out / "csv"
    csv_dir.mkdir(parents=True, exist_ok=True)
    csv_path = csv_dir / "data.csv"
    df.to_csv(csv_path, index=False)
    print("Saved CSV →", csv_path)

    plot_dir = args.out / "plots"

    if len(args.vars) == 1:
        out_png = plot_single(df, args.vars[0], plot_dir)
        print("Saved plot →", out_png)
    else:
        out_png = plot_multi(df, args.vars, plot_dir)
        print("Saved multi-plot →", out_png)

if __name__ == "__main__":
    main()
