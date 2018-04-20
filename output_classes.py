### CLASSES


class STEPS:
    
    def __init__(self):
        ''' Initializes STEPS to empty '''
        self._steps = []

    def set_steps(self, json_dict: dict) -> None:
        ''' Sets self._steps to directions for trip '''
        legs = json_dict["route"]["legs"]
        for leg in legs:
            maneuvers = leg["maneuvers"]
            for dictionary in maneuvers:
                self._steps.append(dictionary["narrative"])

    def display(self) -> None:
        ''' Print directions, 1 line at a time '''
        print()
        print("DIRECTIONS")
        for direction in self._steps:
            print(direction)

    def reply(self, json_dict: dict, elevs: list) -> None:
        ''' Sends complete reply if STEPS is asked for '''
        STEPS.set_steps(self, json_dict)
        STEPS.display(self)
                
        

class TOTALDISTANCE:

    def __init__(self):
        ''' Initializes TOTALDISTANCE to 0 '''
        self._distance = 0

    def set_distance(self, json_dict: dict) -> None:
        ''' Sets self._distance to actual distance of trip '''
        miles = json_dict["route"]["distance"]
        self._distance = float(miles)

    def display(self) -> None:
        ''' Prints total distance required for trip '''
        print()
        print("TOTAL DISTANCE: ", round(self._distance), "miles")

    def reply(self, json_dict: dict, elevs: list) -> None:
        ''' Sends complete reply if TOTALDISTANCE is asked for '''
        TOTALDISTANCE.set_distance(self, json_dict)
        TOTALDISTANCE.display(self)



class TOTALTIME:

    def __init__(self):
        ''' Initializes TOTALTIME to 0 '''
        self._time = 0

    def set_time(self, json_dict: dict) -> None:
        ''' Sets self._time to actual time req for trip '''
        seconds = json_dict["route"]["time"]
        self._time = float(seconds)

    def display(self) -> None:
        ''' Prints total time required for trip '''
        print()
        minutes = self._time/60
        print("TOTAL TIME: ", round(minutes), "minutes")

    def reply(self, json_dict: dict, elevs: list) -> None:
        ''' Sends complete reply if TOTALTIME is asked for '''
        TOTALTIME.set_time(self, json_dict)
        TOTALTIME.display(self)


class LATLONG:

    def __init__(self):
        ''' Initializes LATLONG to empty '''
        self._latlong = []

    def decide_dir(latitude: float, longitude: float) -> list:
        ''' Decides N/S, E/W and return list of both '''
        result = []
        if latitude > 0:
            result.append("N")
        elif latitude < 0:
            result.append("S")
        elif latitude == 0:
            result.append("")
        if longitude > 0:
            result.append("E")
        elif longitude < 0:
            result.append("W")
        elif long_dir == 0:
            result.append("")
        return result

    def set_latlongs(self, json_dict: dict) -> None:
        ''' Appends latlong coordinates to self._latlong for specified locations '''
        locations = json_dict["route"]["locations"]
        for place in locations:
            latlong = place["latLng"]
            latitude = float(latlong["lat"])
            longitude = float(latlong["lng"])
            directions = LATLONG.decide_dir(latitude, longitude)
            coordinate = [latitude, directions[0], longitude, directions[1]]
            self._latlong.append(coordinate)
            
    def display(self) -> None:
        ''' Prints latitudes and longitudes in self._latlong '''
        print()
        print("LATLONGS")
        for coordinate in self._latlong:
            print("{:0.2f}{} {:0.2f}{}".format(abs(coordinate[0]), coordinate[1], abs(coordinate[2]), coordinate[3]))

    def reply(self, json_dict: dict, elevs: list) -> None:
        ''' Sends complete reply if LATLONG is asked for '''    
        LATLONG.set_latlongs(self, json_dict)
        LATLONG.display(self)
        


class ELEVATION:

    def __init__(self):
        ''' Initializes list of ELEVATIONS to empty list '''
        self._elevations = []

    def set_elevations(self, elevs: list) -> None:
        ''' Appends elevations to self._elevation '''
        for elev in elevs:
            self._elevations.append(elev)

    def display(self) -> None:
        ''' Prints elevations for specified locations '''
        print()
        print("ELEVATIONS")
        for elevation in self._elevations:
            print(round(elevation))

    def reply(self, json_dict: dict, elevs: list) -> None:
        ''' Sends complete reply if ELEVATION is asked for '''
        ELEVATION.set_elevations(self, elevs)
        ELEVATION.display(self)


class routeError(Exception):
    pass
