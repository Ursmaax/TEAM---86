
# Simple coordinate dictionary for MVP
# In a real app, use a Geocoding API (e.g., OpenStreetMap / Google Maps)

COORDINATES = {
    "Taiwan": {"lat": 23.6978, "lon": 120.9605},
    "Germany": {"lat": 51.1657, "lon": 10.4515},
    "USA": {"lat": 37.0902, "lon": -95.7129},
    "China": {"lat": 35.8617, "lon": 104.1954},
    "India": {"lat": 20.5937, "lon": 78.9629},
    "UK": {"lat": 55.3781, "lon": -3.4360},
    "Japan": {"lat": 36.2048, "lon": 138.2529},
    "Singapore": {"lat": 1.3521, "lon": 103.8198},
    "Vietnam": {"lat": 14.0583, "lon": 108.2772},
    "Mexico": {"lat": 23.6345, "lon": -102.5528},
    "Default": {"lat": 0.0, "lon": 0.0}
}

def get_coordinates(location_name):
    # Fuzzy matching or direct lookup
    for key in COORDINATES:
        if key.lower() in location_name.lower():
            return COORDINATES[key]
    return COORDINATES["Default"]
