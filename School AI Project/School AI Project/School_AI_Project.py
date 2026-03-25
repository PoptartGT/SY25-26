def search_race(race_name, info_type):  
    with open("races.txt", "r") as file:  
        for line in file:  
            if race_name.lower() in line.lower():  
                data = line.strip().split(",")  # assumes data is comma-separated  
                # Example: [Name, Date, Location, Happened, Standings]  
                labels = ["Name", "Date", "Location", "Happened", "Standings"]  
                info_dict = dict(zip(labels, data))  
                print(info_dict.get(info_type, "Not found"))  
                if info_type == "Happened" and info_dict["Happened"].lower() == "yes":  
                    see_standings = input("See standings? (yes/no): ")  
                    if see_standings.lower() == "yes":  
                        print(info_dict.get("Standings", "No standings info"))  
                return  
        print("Race not found.")  
  
while True:  
    info_type = input("What info do you want to see? (Name/Date/Location/Happened/Standings): ")  
    race_name = input("Enter race name to search: ")  
    search_race(race_name, info_type)  
    again = input("Search another race? (yes/no): ")  
    if again.lower() != "yes":  
        break  

