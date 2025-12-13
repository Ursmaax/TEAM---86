
# Expanded coordinate dictionary for Hackathon Demo
# In production, use Google Maps API or OpenStreetMap Nominatim

COORDINATES = {
    # Major Asian Hubs
    "taiwan": {"lat": 23.6978, "lon": 120.9605},
    "taipei": {"lat": 25.0330, "lon": 121.5654},
    "kaohsiung": {"lat": 22.6273, "lon": 120.3014},
    "china": {"lat": 35.8617, "lon": 104.1954},
    "shanghai": {"lat": 31.2304, "lon": 121.4737},
    "shenzhen": {"lat": 22.5431, "lon": 114.0579},
    "hong kong": {"lat": 22.3193, "lon": 114.1694},
    "singapore": {"lat": 1.3521, "lon": 103.8198},
    "japan": {"lat": 36.2048, "lon": 138.2529},
    "tokyo": {"lat": 35.6762, "lon": 139.6503},
    "india": {"lat": 20.5937, "lon": 78.9629},
    "mumbai": {"lat": 19.0760, "lon": 72.8777},
    "chennai": {"lat": 13.0827, "lon": 80.2707},
    "vietnam": {"lat": 14.0583, "lon": 108.2772},
    "ho chi minh": {"lat": 10.8231, "lon": 106.6297},

    # European Hubs
    "germany": {"lat": 51.1657, "lon": 10.4515},
    "hamburg": {"lat": 53.5511, "lon": 9.9937},
    "rotterdam": {"lat": 51.9244, "lon": 4.4777},
    "uk": {"lat": 55.3781, "lon": -3.4360},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "france": {"lat": 46.2276, "lon": 2.2137},
    "netherlands": {"lat": 52.1326, "lon": 5.2913},

    # North American Hubs
    "usa": {"lat": 37.0902, "lon": -95.7129},
    "united states": {"lat": 37.0902, "lon": -95.7129},
    "los angeles": {"lat": 34.0522, "lon": -118.2437},
    "new york": {"lat": 40.7128, "lon": -74.0060},
    "canada": {"lat": 56.1304, "lon": -106.3468},
    "mexico": {"lat": 23.6345, "lon": -102.5528},

    # Default
    "default": {"lat": 0.0, "lon": 0.0}
}

def get_coordinates(location_name):
    query = location_name.lower().strip()
    
    # 1. Exact Match
    if query in COORDINATES:
        return COORDINATES[query]
    
    # 2. Fuzzy / Partial Match
    for key in COORDINATES:
        if key in query or query in key:
            # Avoid matching "US" in "RUSSIA" type errors generally, but usually ok for demo
            return COORDINATES[key]
            
    return COORDINATES["default"]
