print("welcome to the Py-Fest 2026 manager!")
print("1. View Lineup and Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band By Name")
print("5. Move Band to Specific Position")
print("6. Exit")
choice = input("Enter your choice (1-6): ")

if choice == "1":
   print("\n-------current Lineup-------")
   ("The Rolling Codes - 45 mins - Rock"),
   ("The Debuggers - 30 mins - Pop"),
   ("Syntax Error - 40 mins - metal"),
   ("Null Pointers - 35 mins - Blues"),
   ("Byte Me - 50 mins - Electronic")
   
elif choice == "2":
    print(" ")
    n = input("Enter the name of the new band: ")
    new_time = int(input("Enter the performance time (in minutes): "))
    genre = input("Enter the Genre: ")
    total_time += new_time
    print(f"{new_band} has been added to the lineup.")

elif choice == "6":
    print("Exiting Stage manager. Have a Great Show!")