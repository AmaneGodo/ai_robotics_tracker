# insight_util.py
import json

def compute_basic_stats(df):
    """Return mean, variance, min/max, Weekly change for a city."""
    # in the case of data being empty -> return None for all
    if df.empty:
        return {
            "mean": None, 
            "variance": None, 
            "min": None,
            "max": None, 
            "weekly_change": None,
            "daily_change": None,
            "percent_change": None,
            "first_value": None,
            "last_value": None
        }

    # auto detect the variable (temperaure_2m / wind_speed_10m)
    var = [c for c in df.columns if c != "time"][0]

    # series of data for each variable
    series = df[var]

    # get the first and last value for the comparison
        # .iloc (integer position based indexing) - df[] cant be used so need to specify with .iloc
    first_val = series.iloc[0]
    last_val = series.iloc[-1]

    # TODO: fill logic
    stats = {
        "variables": var,
        "variance": series.var(),
        "mean": series.mean(),
        "min": series.min(),
        "max": series.max(),
        "first_val": first_val,
        "second_val":  last_val,
        "weekly_change": last_val - first_val,   
        "percent_change": ((last_val - first_val) / first_val) * 100 if first_val != 0 else None
    }

    return stats


def generate_insights(city_name, stats):
    """Return natural-language insights based on stats dictionary."""
    insights = []
    var = stats["variables"]

    is_temp = ("temp" in var.lower())

    weekly_change = stats["weekly_change"]

    # Weekly trend - change in temperature over the week
    if is_temp:
        if stats["weekly_change"] > 0:
            insights.append(f"{city_name} warmed by {stats['weekly_change']:.1f} C over the week.")
        elif stats["weekly_change"] < 0:
            insights.append(f"{city_name} cooled by {abs(stats['weekly_change']):.1f} C over the week.")
        else:
            insights.append(f"{city_name}")

    else:
        if weekly_change > 0:
            insights.append(f"{var} in {city_name} increased by {weekly_change}")
        elif weekly_change < 0:
            insights.append(f"{var} in {city_name} decreased by {weekly_change}")
        else:
            insights.append(f"No change in {var} over the week")

    # Weekly trend - variance
    if stats["variance"] > 5:
        insights.append(f"{city_name} shows high variance in {var}.")
    elif stats["variance"] > 2:
        insights.append(f"{city_name} shows moderate variance in {var}")
    else:
        insights.append(f"{city_name} shows stable {var} (low variance).")

    insights.append(f"{city_name}'s {var} ranged from {stats['min']:.1f} C to {stats['max']:.1f} C.")

    return insights

def save_insights(city_name, stats, insights, out_dir):
    """Save insights + stats to a TXT and JSON file."""

    txt_dir = out_dir / "text"
    json_dir = out_dir / "json"

    txt_dir.mkdir(parents=True, exist_ok=True)
    json_dir.mkdir(parents=True, exist_ok=True)
    # saving the txt file
    txt_path = txt_dir / f"{city_name}_weekly_insights.txt"
    with open(txt_path, "w") as f:
        f.write(
            f"Weekly Summary for {city_name}\n"
            f"Variable of the insight - {stats["variables"]}\n"
            f"===============================================\n\n"


            f"Mean:             {stats['mean']:.1f}\n"
            f"Variance:         {stats['variance']:.1f}\n"
            f"Min:              {stats['min']:.1f}\n"
            f"Max:              {stats['max']:.1f}\n"
            f"Weekly change:    {stats['weekly_change']:.2f}\n"
        )
        
        if stats["percent_change"] is not None:
            f.write(
                f"Percent Change:   {stats['percent_change']:.2f}%\n"
            )

        f.write(
            f"Insights:\n"
        )

        for ins in insights:
            f.write(f"- {ins}\n")

    print(f"Saved the txt file -> {txt_path}")
    
    # saving the json file
    json_path = json_dir / f"{city_name}_weekly.json"
    json_data = {
        "city": city_name, 
        "variables": stats['variables'],
        "stats": stats,
        "insights": insights 
    }

    with open(json_path, "w") as jf:
        json.dump(json_data, jf, indent = 4)

    print(f"Saved Json insights -> {json_path}")
