import argparse
from pathlib import Path
from .data_handler import build_url, fetch_json, to_dataframe, fetch_city_dataframe
from .plot_util import plot_single, plot_multi, ensure_plot_dir
from .insight_util import compute_basic_stats, generate_insights, save_insights

PROJECT_NAME = "api_plotter"
DEFAULT_OUT = Path(f"data/projects/{PROJECT_NAME}")
CITY_COORDS = {
    "Tokyo"         : (35.68, -40.31),
    "Boston"        : (42.36, -71.06),
    "London"        : (51.51, -0.13),
}

def get_args():
    p = argparse.ArgumentParser(description="Open-Meteo plotter")

    # get names of cities for the plot
    p.add_argument("--cities", nargs="+", help="List of city names", required=True)

    # get latitude and longitude from the input
    #p.add_argument("--lat", type=float, default=42.36, help="Latitude")
    #p.add_argument("--lon", type=float, default=-71.06, help="Longitude")

    # get the variable to fetch from the input
    p.add_argument("--vars", nargs="+", default=["temperature_2m"], help="Variables to fetch")

    # get the folder path to save the csv and plot png
    p.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output folder")

    p.add_argument("--insights", action="store_true",
                   help="Generate insights text files for each city")
    return p.parse_args()

def get_city_coords(city_name: str):
    try: 
        return CITY_COORDS[city_name]
    except KeyError:
        data_coords = ", ".join(CITY_COORDS.keys())
        raise KeyError(f"{city_name} is not in our data. Cities available are {data_coords}")

# def main():
#     args = get_args()

#     url = build_url(args.lat, args.lon, args.vars)
#     print("Fetching:", url)
#     payload = fetch_json(url)

#     df = to_dataframe(payload, args.vars)

#     csv_dir = args.out / "csv"
#     csv_dir.mkdir(parents=True, exist_ok=True)
#     csv_path = csv_dir / "data.csv"
#     df.to_csv(csv_path, index=False)
#     print("Saved CSV →", csv_path)

#     plot_dir = args.out / "plots"

#     if len(args.vars) == 1:
#         out_png = plot_single(df, args.vars[0], plot_dir)
#         print("Saved plot →", out_png)
#     else:
#         out_png = plot_multi(df, args.vars, plot_dir)
#         print("Saved multi-plot →", out_png)

def run():
    args = get_args()

    print("variables: ", args.vars)
    print("cities: ", args.cities)
    print("out: ", args.out)

    # prepare output directories
    csv_root = args.out / "csv"
    csv_root.mkdir(parents=True, exist_ok=True)

    insights_root = args.out / "insights"
    insights_root.mkdir(parents=True, exist_ok=True)

    df_cities = {}
    for city in args.cities:
        # get lat and lon from the city
        lat, lon = get_city_coords(city)

        # construct the dataframe using the function we just made and save 
        df = fetch_city_dataframe(city, lon, lat, args.vars)
        df_cities[city] = df

        stats = compute_basic_stats(df)
        insights = generate_insights(city, stats)
        save_insights(city, stats, insights, insights_root)

        # save csv per city
        csv_path = csv_root / f"{city}.csv"
        df.to_csv(csv_path, index=False)
        print(f"Saved CSV for {city} -> {csv_path}")

    plot_root = args.out / "plots"

    for var in args.vars:
        out_dir = ensure_plot_dir(plot_root, var)

        # single-city plots
        for city, df in df_cities.items():
            out_png = plot_single(city, df, var, out_dir)
            print(f"Individual plot - {out_png} has been saved")

        multi_png = plot_multi(df_cities, var, out_dir)
        print(f"Multi-plot - {multi_png} has been saved")

def main():
    run()

if __name__ == "__main__":
    main()
