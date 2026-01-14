
def display_menu():
    print("\nwelcome to the Py-Fest 2026 manager!")
    print("1. View Lineup and Total Time")
    print("2. Add a New Band")
    print("3. Move First Band to End (Late Arrival)")
    print("4. Remove a Band By Name")
    print("5. Move Band to Specific Position")
    print("6. Exit")

def view_lineup(bands):
    if not bands:
        print("\nThe lineup is currently empty.")
        return
    
    print("\n--- Current Lineup ---")
    total_time = 0
    for i, band in enumerate(bands, 1):
        print(f"{i}. {band['name']} - {band['time']} mins - {band['genre']}")
        total_time += band['time']
    print(f"Total Festival Time: {total_time} minutes")

def add_band(bands):
    name = input("Enter band name: ")
    try:
        time = int(input("Enter performance time (mins): "))
        genre = input("Enter genre: ")
        bands.append({"name": name, "time": time, "genre": genre})
        print(f"Added {name} to the lineup.")
    except ValueError:
        print("Invalid time. Please enter a number.")

def move_first_to_end(bands):
    if len(bands) < 2:
        print("Not enough bands to move.")
        return
    first_band = bands.pop(0)
    bands.append(first_band)
    print(f"Moved {first_band['name']} to the end of the lineup.")

def remove_band(bands):
    name = input("Enter the name of the band to remove: ")
    for i, band in enumerate(bands):
        if band['name'].lower() == name.lower():
            removed = bands.pop(i)
            print(f"Removed {removed['name']} from the lineup.")
            return
    print(f"Band '{name}' not found.")

def move_to_position(bands):
    if not bands:
        print("The lineup is empty.")
        return
    
    name = input("Enter the name of the band to move: ")
    band_to_move = None
    for i, band in enumerate(bands):
        if band['name'].lower() == name.lower():
            band_to_move = bands.pop(i)
            break
    
    if not band_to_move:
        print(f"Band '{name}' not found.")
        return

    try:
        pos = int(input(f"Enter new position (1-{len(bands) + 1}): "))
        if 1 <= pos <= len(bands) + 1:
            bands.insert(pos - 1, band_to_move)
            print(f"Moved {band_to_move['name']} to position {pos}.")
        else:
            bands.append(band_to_move) # Put it back if invalid
            print("Invalid position.")
    except ValueError:
        bands.append(band_to_move) # Put it back if invalid
        print("Invalid input. Position must be a number.")

def main():
    # Initial bands from the provided image
    bands = [
        {"name": "The Rolling Codes", "time": 45, "genre": "Rock"},
        {"name": "The Debuggers", "time": 30, "genre": "Pop"},
        {"name": "Syntax Error", "time": 40, "genre": "metal"},
        {"name": "Null Pointers", "time": 35, "genre": "Blues"},
        {"name": "Byte Me", "time": 50, "genre": "Electronic"}
    ]

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            view_lineup(bands)
        elif choice == '2':
            add_band(bands)
        elif choice == '3':
            move_first_to_end(bands)
        elif choice == '4':
            remove_band(bands)
        elif choice == '5':
            move_to_position(bands)
        elif choice == '6':
            print("Exiting Py-Fest 2026 manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
Manus
