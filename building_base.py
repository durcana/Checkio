#Input: Statements and expression with the Building class.
#Output: The behaviour as described.


class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {"north-west": [self.width_NS + self.south, self.west],
                "north-east": [self.width_NS + self.south, self.width_WE + self.west],
                "south-west": [self.south, self.west],
                "south-east": [self.south, self.width_WE + self.west]
        }

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.width_WE * self.width_NS * self.height

    def __repr__(self):
        return str("Building(" + str(self.south) + ", " + str(self.west) + ", " 
                + str(self.width_WE) + ", " + str(self.width_NS) + ", " + 
                str(self.height) + ")")
