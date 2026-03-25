seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 
           'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']

# Ask user for seed input
user_seed = int(input("Enter a seed number (1-16): "))

# Check and print the Cinderella alert only for the team with the input seed
for seed, team in zip(seeds, winners):
    if seed == user_seed and seed >= 10:
        print(f"Cinderella Alert! {team} pulls the upset")
        break
else:
    print(f"No Cinderella alert for seed {user_seed} or seed is below 10.")


