import matplotlib.pyplot as plt
from pathlib import Path

def ensure_plot_dir(root: Path, var: str) -> Path:
    """
    Ensure folder like plots/temperature_2m/ exists.
    Returns full directoory path
    """

    out_dir = root / var
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir

def plot_single(city: str, df, variable: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 4))
    plt.plot(df["time"], df[variable], label=city, linewidth = 2)

    plt.xticks(rotation=30, ha="right")
    plt.xlabel("Time")
    plt.ylabel(variable)
    plt.title(f"{city} - {variable} (24h)")
    plt.grid(True)
    plt.legend()

    out_path = out_dir / f"{city}.png"
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    return out_path

def plot_multi(df_cities: dict, var: str, out_dir: Path):
    plt.figure(figsize=(10, 5))

    for city, df in df_cities.items():
        plt.plot(df["time"], df[var], label=city, linewidth=2)

    plt.title(f"Muti-City comparison - {var}")
    plt.xlabel("time")
    plt.ylabel(var)
    plt.grid(True)
    plt.legend()

    out_path = out_dir / "multi_plot.png"
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    return out_path