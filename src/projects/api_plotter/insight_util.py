# insight_util.py

def compute_basic_stats(df):
    """Return mean, variance, min/max, Weekly change for a city."""
    stats = {}

    if df.empty:
        return {"mean": None, "variance": None, "min": None,
            "max": None, "weekly_change": None}

    var = "temperature_2m"
    # TODO: fill logic
    stats["mean"] = df[var].mean()
    stats["variance"] = df[var].var()
    stats["min"] = df[var].min()
    stats["max"] = df[var].max()
    stats["weekly_change"] = df[var].iloc[-1] - df[var].iloc[0]

    return stats


def generate_insights(city_name, stats):
    """Return natural-language insights based on stats dictionary."""
    insights = []

    # TODO: 
    if stats["weekly_change"] > 0:
        insights.append(f"{city_name} warmed by {stats['weekly_change']:.1f} C over the week.")
    else:
        insights.append(f"{city_name} cooled by {abs(stats['weekly_change']):.1f} C over the week.")

    if stats["variance"] > 2:
        insights.append(f"{city_name} shows high variance in temperature (unstable weather).")
    else:
        insights.append(f"{city_name} shows stable weather (low variance).")

    insights.append(f"{city_name} temperature ranged from {stats['min']:.1f} C to {stats['max']:.1f} C.")

    return insights

def save_insights(city_name, stats, insights, out_dir):
    """Save insights + stats to a TXT or JSON file."""
    # TODO: create file here
    filepath = out_dir / f"{city_name}_insights.txt"
    with open(filepath, "w") as f:
        f.write(
            f"Mean:             {stats['mean']:.1f}\n"
            f"Variance:         {stats['variance']:.1f}\n"
            f"Min:              {stats['min']:.1f}\n"
            f"Max:              {stats['max']:.1f}\n"
            f"Weekly change:    {stats['weekly_change']:.1f}\n"
        )

        for ins in insights:
            f.write(f"- {ins}\n")

