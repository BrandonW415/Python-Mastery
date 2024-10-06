
def print_action(action):
    print(action)
    
def start_engine():
    print_action("Starting the engine.")

def stop_engine():
    print_action("Stopping the engine.")
    
def move_forward():
    print_action("Moving forward.")
    
def turn(direction):
    print_action(f"Turning {direction}.")
    
def enter_roundabout():
    print_action(f"Entering the roundabout.")
    
def take_exit(exit_number):
    print_action(f"Taking the {exit_number} exit.")
    
def announce_arrival(destination):
    print_action(f"You have arrived at the {destination}.")
    
def navigate_from_center(destination):
    move_forward()
    if destination == "library":
        turn("left")
    elif destination == "tech park":
        turn("right")
    else:
        enter_roundabout()
        return True
    return False

def navigate_from_roundabout(destination):
    roundabout_exits = {
        "hospital": ("1st", None),
        "mall": ("2nd", "right"),
        "airport": ("3rd", None),
        "university": ("4th", "left"),
        "stadium": ("4th", "right")
    }
    
    if destination in roundabout_exits:
        exit_num, additional_turn = roundabout_exits[destination]
        take_exit(exit_num)
        if additional_turn:
            move_forward()
            turn(additional_turn)
    else:
        print_action(f"Error: '{destination}' is not a recognized destination.")
        return False
    return True

def navigate_to_destination(destination):
    if navigate_from_center(destination):
        navigate_from_roundabout(destination)
    announce_arrival(destination)
    
def main():
    start_engine()
    destination = input("Please enter your desired destination: ").lower()
    navigate_to_destination(destination)
    stop_engine()
    
if __name__ == "__main__":
    main()