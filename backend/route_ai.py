import math

from route_data import cold_storages

# ==========================================
# Distance Formula (Haversine)
# ==========================================

def calculate_distance(lat1, lon1, lat2, lon2):

    R = 6371

    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)

    a = (
        math.sin(dLat / 2) ** 2
        +
        math.cos(math.radians(lat1))
        *
        math.cos(math.radians(lat2))
        *
        math.sin(dLon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c

# ==========================================
# Find Nearest Cold Storage
# ==========================================

def find_best_route(current_lat, current_lon):

    nearest = None

    minimum_distance = 999999

    for storage in cold_storages:

        distance = calculate_distance(

            current_lat,

            current_lon,

            storage["latitude"],

            storage["longitude"]

        )

        if distance < minimum_distance:

            minimum_distance = distance

            nearest = storage

    eta = max(
        1,
        round(minimum_distance / 40 * 60)
    )

    return {

        "destination": nearest["name"],

        "latitude": nearest["latitude"],

        "longitude": nearest["longitude"],

        "distance": round(minimum_distance, 2),

        "eta": eta

    }