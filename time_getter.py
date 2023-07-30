import requests
import pygame as pg

def request(timezone: str):
    #url must be with the timezone from the city
    api_url = f'https://timeapi.io/api/Time/current/zone?timeZone={timezone}'
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == requests.codes.ok:
        return int(data["hour"]), int(data["minute"])
    else:
        return False, data["status"], data["errors"]