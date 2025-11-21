import requests
import pandas as pd

def build_url(lat:float, lon:float, variables: list[str]) -> str:
    items = ",".join(variables)
    return (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&hourly={items}&past_days=1"       
    )

def fetch_json(url:str) -> dict:
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    return r.json()

def to_dataframe(payload: dict, variables:list[str]) -> pd.DataFrame:
    df = pd.DataFrame()
    df['time'] = pd.to_datetime(payload['hourly']['time'])

    for var in variables:
        df[var] = payload["hourly"][var]

    df = df.dropna().reset_index(drop=True)
    return df

def fetch_city_dataframe(city: str, lon: float, lat: float, vars_list: list) -> pd.DataFrame:
    url = build_url(lat, lon, vars_list)
    print(f"fetching [{city}] -> {url}")

    payload = fetch_json(url)
    df = to_dataframe(payload, vars_list)

    return df