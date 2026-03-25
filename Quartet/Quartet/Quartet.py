F1 = ["F1", "VW Off-Road-Bug", 185, (104,142), 6000, 9, 1880, 4]
H2 = ["H2", "Mitsubishi Lancer", 198, (213,290), 5500, 7.2, 1997, 4]
D4 = ["D4", "Peugeot 206 WRC", 225, (221,300), 5600, 5.4, 1996, 4]
E4 = ["E4", "Austin Metro 6", 240, (265,360), 9800, 3.4, 3600, 6]
D3 = ["D3", "Seat Toledo Marathon", 220, (195,330), 8400, 5.2, 2100, 5]
F2 = ["F2", "Mitsubishi Galant", 180, (216,294), 5800, 6.3, 3395, 4]
E1 = ["E1", "Mitsubishi Carisma GT", 225, (213,290), 6000, 5.2, 1996, 4]
F3 = ["F3", "Renault Megane", 218, (198,270), 8400, 5.9, 1995, 4]
G4 = ["G4", "Fiat Punto Kit-Car", 165, (161,220), 7500, 9.8, 1600, 4]
D2 = ["D2", "Toyota Celica GT-Four", 245, (220,299), 5600, 5.3, 1998, 4]
E3 = ["E3", "Skoda Octavia WRC", 230, (221,300), 7500, 5.3, 2000, 4]
G2 = ["G2", "Seat Ibiza GTi", 185, (104,142), 6000, 9, 1880, 4]

cars = [F1, H2, D4, E4, D3, F2, E1, F3, G4, D2, E3, G2]

def print_car(c):
    print("Car:", c[1])
    print(":", c[2])
    print(":", c[3])
    print(":", c[4])
    print(":", c[5])
    print(":", c[6])

i = 1
for car in cars:
    print(i, car[1])
    i += 1

choice = int(input("which car: "))
print_car(cars[choice - 1])