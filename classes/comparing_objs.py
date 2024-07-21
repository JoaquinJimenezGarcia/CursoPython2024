class Coordinates:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
    
    def __ne__(self, other):
        return self.lat != other.lat or self.lon != other.lon
    
    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon
    
    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon



coords1 = Coordinates(45, 27)
coords2 = Coordinates(45, 27)
coords3 = Coordinates(48, 30)

print(coords1 == coords2)
print(coords1 != coords2)
print(coords2<coords3)
print(coords1<=coords3)