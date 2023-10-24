#Opens file and establishes layout
with open('C:\\Users\\dbutt\\OneDrive\\Desktop\\cse110\\week-11\\le.csv') as data_set:
    for row in data_set:
        row = row.split(",")

        country = row[0].strip()
        code = row[1].strip()
        year = row[2].strip()
        life_expectancy = (row[3])

        max_life = -1
        min_life = (life_expectancy)
        avg_life = (life_expectancy) / len(life_expectancy)

        max_country = ""
        max_year = max(year)
        min_country = min(country)
        min_year = min(year)

        chosen_year = ""

#Tells user to enter year
year_lookup = input(float("Enter the year of interest: "))

#Generates three expectancy outputs
if chosen_year == year_lookup:
    chosen_year = year_lookup
    print(f"For the year: {year_lookup}.\n")
    print(f"The average life expectancy across all countries was str{avg_life:.2f}\n")
    print(f"The max life expectancy was in {max_country} with {max_life:.2f}\n")
    print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")

    #Uses a nested-if statement to store averages to display in output
    if life_expectancy > max_life:
        max_life = life_expectancy
        max_country = country

    #prints the above
    print()
    print(f"The overall max life expectancy is:{max_life:.2f} from {max_country} in {max_year:.2f}.\n")
    print(f"The overall min life expectancy is:{min_life:.2f} from {min_country} in {min_year:.2f}.\n")