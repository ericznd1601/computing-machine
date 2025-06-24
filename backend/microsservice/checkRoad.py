import requests
def get_surface_type(lat, lon):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    way(around:50,{lat},{lon})["highway"]["surface"];
    out body;
    """
    response = requests.post(overpass_url, data=query)
    data = response.json()

    surfaces = [way["tags"].get("surface") for way in data.get("elements", []) if "tags" in way]

    if not surfaces:
        return "unknown"
    return max(set(surfaces), key=surfaces.count)
