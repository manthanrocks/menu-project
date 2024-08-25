import geocoder

def get_location():
    g = geocoder.ip('me')
    return g.latlng, g.address

# Example usage
coordinates, address = get_location()
print(f'Coordinates: {coordinates}')
print(f'Address: {address}')
