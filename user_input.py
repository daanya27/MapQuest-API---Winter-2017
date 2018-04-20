import mapquest_api
import output_classes
import urllib.error


### READING INPUT


def read_input() -> list:
    ''' Reads input, assuming it is valid, and returns list of all inputs '''
    input_list = []
    locations = []
    expected_outputs = []
    
    number_locations = int(input())
    input_list.append(number_locations)
    
    for location in range(number_locations):
        locations.append(input().strip())
    input_list.append(locations)
    
    number_outputs = int(input())
    input_list.append(number_outputs)
    
    for output in range(number_outputs):
        expected_outputs.append(input().strip())
    input_list.append(expected_outputs)
    
    return input_list


def handle_output(input_list: list, json_dict: dict) -> None:
    ''' Depending on output specified, handles output '''

    if json_dict["info"]["statuscode"] == 402:
        raise output_classes.routeError()
    
    expected_outputs = input_list[-1]
    elevs = None

    for output in expected_outputs:
        
        if output == "STEPS":
            output_type = output_classes.STEPS()
        elif output == "TOTALDISTANCE":
            output_type = output_classes.TOTALDISTANCE()
        elif output == "TOTALTIME":
            output_type = output_classes.TOTALTIME()
        elif output == "LATLONG":
            output_type = output_classes.LATLONG()
        elif output == "ELEVATION":
            elevs = mapquest_api.build_elev_url(input_list, json_dict)
            output_type = output_classes.ELEVATION()

        output_type.reply(json_dict, elevs)


def print_copyright() -> None:
    ''' Prints required copyright line '''
    print()
    print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")


def main_function() -> None:
    ''' Runs main program/UI '''
   
    try:
        input_list = read_input()
        url = mapquest_api.build_url(input_list)
        json_dict = mapquest_api.read_url(url)
        handle_output(input_list, json_dict)

    except urllib.error.HTTPError:
        print()
        print("MAPQUEST ERROR")

    except output_classes.routeError:
        print()
        print("NO ROUTE FOUND")
        
    except Exception:
        if json_dict["info"]["statuscode"] != 0: #other non-HTTP mapquest errors
            print()
            print("MAPQUEST ERROR")
        else:
            print()
            print("ERROR") 
    
    finally:
        print_copyright()
            

            
if __name__ == "__main__":
    main_function()
    


"""
TEST:
5
Oklahoma City, Oklahoma
Houston, Texas
Austin, Texas
Ashland, Oregon
Mexico City, Mexico
5
STEPS
LATLONG
ELEVATION
TOTALTIME
TOTALDISTANCE
"""
