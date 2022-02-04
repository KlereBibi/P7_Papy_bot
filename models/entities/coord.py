"""module to creat object coordonate """

class Coord:

    """class to create the coordonate"""

    def __init__(self, lat, lon, add):

        """args: (int) latitude
                 (int) longitude
                 (str)  adresse"""

        self.latitude = lat
        self.longitude = lon
        self.adress = add
