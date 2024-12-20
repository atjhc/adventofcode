from enum import Flag

class Fences(Flag):
    NONE  = 0b0000
    NORTH = 0b0001
    EAST  = 0b0010
    SOUTH = 0b0100
    WEST  = 0b1000

    def hasSide(self, side):
        return (self & side) == side


class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def north(self):
        return Location(self.x, self.y - 1)

    def east(self):
        return Location(self.x + 1, self.y)

    def south(self):
        return Location(self.x, self.y + 1)

    def west(self):
        return Location(self.x - 1, self.y)

    def __repr__(self):
        return f"({x}, {y})"

class Garden:
    @classmethod
    def fromFile(klass, filePath):
        with open(filePath, 'r') as file:
            data = [[Plot(value) for value in list(line.strip())] for line in file]
        height = len(data)
        width = len(data[0]) if height > 0 else 0
        instance = klass(width, height, None)
        instance.data = data
        return instance

    def __init__(self, width, height, defaultValue=None):
        self.data = [[defaultValue for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height

    def value(self, location):
        if not self.inBounds(location):
            return None
        return self.data[location.y][location.x]

    def setValue(self, location, value):
        self.data[location.y][location.x] = value

    def inBounds(self, location):
        if location.x < 0 or location.x >= self.width:
            return False
        if location.y < 0 or location.y >= self.height:
            return False
        return True

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return '\n'.join([''.join(map(str, row)) for row in self.data])

class Plot:
    @classmethod
    def fromInput(klass, input):
        return klass(input)

    def __init__(self, type):
        self.type = type
        self.fences = Fences.NONE
        self.region = None

    def __repr__(self):
        if self.fences != Fences.NONE:
            return '*'
        return self.type

class Region:
    def __init__(self, type):
        self.type = type
        self.plots = []

garden = Garden.fromFile("input.txt")
regions = []

def populate(plot, location, region=None):
    if plot.region != None:
        return
    if region == None:
        region = Region(plot.type)
        regions.append(region)
    plot.region = region
    region.plots.append(plot)
    northPlot = garden.value(location.north())
    if northPlot != None and northPlot.type == plot.type:
        populate(northPlot, location.north(), region)
    else:
        plot.fences |= Fences.NORTH
    eastPlot = garden.value(location.east())
    if eastPlot != None and eastPlot.type == plot.type:
        populate(eastPlot, location.east(), region)
    else:
        plot.fences |= Fences.EAST
    southPlot = garden.value(location.south())
    if southPlot != None and southPlot.type == plot.type:
        populate(southPlot, location.south(), region)
    else:
        plot.fences |= Fences.SOUTH
    westPlot = garden.value(location.west())
    if westPlot != None and westPlot.type == plot.type:
        populate(westPlot, location.west(), region)
    else:
        plot.fences |= Fences.WEST

for y, row in enumerate(garden):
    for x, _ in enumerate(row):
        location = Location(x, y)
        plot = garden.value(location)
        populate(plot, location)

total = 0
for region in regions:
    sides = 0
    for y in range(garden.height):
        northFence = False
        southFence = False
        for x in range(garden.width):
            plot = garden.value(Location(x, y))
            # Skip if this plot isn't in the region under consideration
            if plot.region != region:
                if northFence:
                    northFence = False
                    sides += 1
                if southFence:
                    southFence = False
                    sides += 1
                continue
            if northFence and not plot.fences.hasSide(Fences.NORTH):
                northFence = False
                sides += 1
            elif plot.fences.hasSide(Fences.NORTH):
                northFence = True
            if southFence and not plot.fences.hasSide(Fences.SOUTH):
                southFence = False
                sides += 1
            elif plot.fences.hasSide(Fences.SOUTH):
                southFence = True
        if northFence:
            sides += 1
        if southFence:
            sides += 1

    for x in range(garden.width):
        westFence = False
        eastFence = False
        for y in range(garden.height):
            plot = garden.value(Location(x, y))
            if plot.region != region:
                if westFence:
                    westFence = False
                    sides += 1
                if eastFence:
                    eastFence = False
                    sides += 1
                continue
            if westFence and not plot.fences.hasSide(Fences.WEST):
                westFence = False
                sides += 1
            elif plot.fences.hasSide(Fences.WEST):
                westFence = True
            if eastFence and not plot.fences.hasSide(Fences.EAST):
                eastFence = False
                sides += 1
            elif plot.fences.hasSide(Fences.EAST):
                eastFence = True
        if westFence:
            sides += 1
        if eastFence:
            sides += 1
    print(f"region {region.type}: {sides}")
    total += len(region.plots) * sides
print(total)