import matplotlib.pyplot as plt
from pathlib import Path

def plot_single(df, variable, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 4))
    plt.plot(df["time"], df[variable], label=variable)
    plt.xticks(rotation=30, ha="right")
    plt.xlabel("Time")
    plt.ylabel(variable)
    plt.title(f"{variable} over last 24 hours")
    plt.grid(True)
    plt.legend()

    out_path = out_dir / f"{variable}.png"
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
    return out_path

def plot_multi(df, variables, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(len(variables), 1, figsize=(8, 4*len(variables)))
    if len(variables) == 1:
        axes = [axes]

    for ax, var in zip(axes, variables):
        ax.plot(df["time"], df[var])
        ax.set_title(var)
        ax.grid(True)
        ax.set_xlabel("Time")
        ax.set_ylabel(var)

    plt.tight_layout()
    out_path = out_dir / "multi_plot.png"
    plt.savefig(out_path)
    plt.close()
    return out_path