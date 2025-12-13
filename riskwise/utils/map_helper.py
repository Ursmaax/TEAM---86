
# Expanded coordinate dictionary for Hackathon Demo
# In production, use Google Maps API or OpenStreetMap Nominatim


# Expanded Global Coordinate Database for Hackathon Demo
# Includes major countries and logistics hubs.

COORDINATES = {
    # --- ASIA ---
    "taiwan": {"lat": 23.6978, "lon": 120.9605}, "taipei": {"lat": 25.0330, "lon": 121.5654},
    "china": {"lat": 35.8617, "lon": 104.1954}, "shanghai": {"lat": 31.2304, "lon": 121.4737}, "beijing": {"lat": 39.9042, "lon": 116.4074}, "shenzhen": {"lat": 22.5431, "lon": 114.0579}, "guangzhou": {"lat": 23.1291, "lon": 113.2644}, "hong kong": {"lat": 22.3193, "lon": 114.1694},
    "india": {"lat": 20.5937, "lon": 78.9629}, "mumbai": {"lat": 19.0760, "lon": 72.8777}, "delhi": {"lat": 28.7041, "lon": 77.1025}, "bangalore": {"lat": 12.9716, "lon": 77.5946}, "chennai": {"lat": 13.0827, "lon": 80.2707}, "hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "japan": {"lat": 36.2048, "lon": 138.2529}, "tokyo": {"lat": 35.6762, "lon": 139.6503}, "osaka": {"lat": 34.6937, "lon": 135.5023},
    "south korea": {"lat": 35.9078, "lon": 127.7669}, "seoul": {"lat": 37.5665, "lon": 126.9780}, "busan": {"lat": 35.1796, "lon": 129.0756},
    "singapore": {"lat": 1.3521, "lon": 103.8198},
    "vietnam": {"lat": 14.0583, "lon": 108.2772}, "ho chi minh": {"lat": 10.8231, "lon": 106.6297}, "hanoi": {"lat": 21.0285, "lon": 105.8542},
    "thailand": {"lat": 15.8700, "lon": 100.9925}, "bangkok": {"lat": 13.7563, "lon": 100.5018},
    "malaysia": {"lat": 4.2105, "lon": 101.9758}, "kuala lumpur": {"lat": 3.1390, "lon": 101.6869},
    "indonesia": {"lat": -0.7893, "lon": 113.9213}, "jakarta": {"lat": -6.2088, "lon": 106.8456},
    "philippines": {"lat": 12.8797, "lon": 121.7740}, "manila": {"lat": 14.5995, "lon": 120.9842},
    "uae": {"lat": 23.4241, "lon": 53.8478}, "dubai": {"lat": 25.2048, "lon": 55.2708}, "abu dhabi": {"lat": 24.4539, "lon": 54.3773},
    "saudi arabia": {"lat": 23.8859, "lon": 45.0792}, "riyadh": {"lat": 24.7136, "lon": 46.6753},

    # --- EUROPE ---
    "germany": {"lat": 51.1657, "lon": 10.4515}, "berlin": {"lat": 52.5200, "lon": 13.4050}, "hamburg": {"lat": 53.5511, "lon": 9.9937}, "frankfurt": {"lat": 50.1109, "lon": 8.6821}, "munich": {"lat": 48.1351, "lon": 11.5820},
    "uk": {"lat": 55.3781, "lon": -3.4360}, "london": {"lat": 51.5074, "lon": -0.1278}, "manchester": {"lat": 53.4808, "lon": -2.2426},
    "france": {"lat": 46.2276, "lon": 2.2137}, "paris": {"lat": 48.8566, "lon": 2.3522}, "marseille": {"lat": 43.2965, "lon": 5.3698},
    "italy": {"lat": 41.8719, "lon": 12.5674}, "rome": {"lat": 41.9028, "lon": 12.4964}, "milan": {"lat": 45.4642, "lon": 9.1900},
    "spain": {"lat": 40.4637, "lon": -3.7492}, "madrid": {"lat": 40.4168, "lon": -3.7038}, "barcelona": {"lat": 41.3851, "lon": 2.1734},
    "netherlands": {"lat": 52.1326, "lon": 5.2913}, "amsterdam": {"lat": 52.3676, "lon": 4.9041}, "rotterdam": {"lat": 51.9244, "lon": 4.4777},
    "belgium": {"lat": 50.5039, "lon": 4.4699}, "brussels": {"lat": 50.8503, "lon": 4.3517}, "antwerp": {"lat": 51.2194, "lon": 4.4025},
    "switzerland": {"lat": 46.8182, "lon": 8.2275}, "zurich": {"lat": 47.3769, "lon": 8.5417},
    "sweden": {"lat": 60.1282, "lon": 18.6435}, "stockholm": {"lat": 59.3293, "lon": 18.0686},
    "poland": {"lat": 51.9194, "lon": 19.1451}, "warsaw": {"lat": 52.2297, "lon": 21.0122},

    # --- AMERICAS ---
    "usa": {"lat": 37.0902, "lon": -95.7129}, "united states": {"lat": 37.0902, "lon": -95.7129},
    "new york": {"lat": 40.7128, "lon": -74.0060}, "los angeles": {"lat": 34.0522, "lon": -118.2437}, "chicago": {"lat": 41.8781, "lon": -87.6298}, "houston": {"lat": 29.7604, "lon": -95.3698}, "miami": {"lat": 25.7617, "lon": -80.1918}, "san francisco": {"lat": 37.7749, "lon": -122.4194}, "seattle": {"lat": 47.6062, "lon": -122.3321},
    "canada": {"lat": 56.1304, "lon": -106.3468}, "toronto": {"lat": 43.6532, "lon": -79.3832}, "vancouver": {"lat": 49.2827, "lon": -123.1207}, "montreal": {"lat": 45.5017, "lon": -73.5673},
    "mexico": {"lat": 23.6345, "lon": -102.5528}, "mexico city": {"lat": 19.4326, "lon": -99.1332},
    "brazil": {"lat": -14.2350, "lon": -51.9253}, "sao paulo": {"lat": -23.5505, "lon": -46.6333}, "rio de janeiro": {"lat": -22.9068, "lon": -43.1729},
    "argentina": {"lat": -38.4161, "lon": -63.6167}, "buenos aires": {"lat": -34.6037, "lon": -58.3816},
    "chile": {"lat": -35.6751, "lon": -71.5430}, "santiago": {"lat": -33.4489, "lon": -70.6693},

    # --- AFRICA / OCEANIA ---
    "australia": {"lat": -25.2744, "lon": 133.7751}, "sydney": {"lat": -33.8688, "lon": 151.2093}, "melbourne": {"lat": -37.8136, "lon": 144.9631},
    "new zealand": {"lat": -40.9006, "lon": 174.8860}, "auckland": {"lat": -36.8485, "lon": 174.7633},
    "south africa": {"lat": -30.5595, "lon": 22.9375}, "johannesburg": {"lat": -26.2041, "lon": 28.0473}, "cape town": {"lat": -33.9249, "lon": 18.4241},
    "egypt": {"lat": 26.8206, "lon": 30.8025}, "cairo": {"lat": 30.0444, "lon": 31.2357},
    "nigeria": {"lat": 9.0820, "lon": 8.6753}, "lagos": {"lat": 6.5244, "lon": 3.3792},
    
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
