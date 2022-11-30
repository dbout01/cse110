#Gets path to use in with statement
import pathlib
cwd = pathlib.Path(__file__).parent.resolve()
le = f'{cwd}/le.csv'


max_life = 0


#Opens file and establishes layout
with open(le) as data_set:
    next(data_set)
    for row in data_set:
        row = row.split(",")

        country = row[0].strip()
        code = row[1].strip()
        year = row[2].strip()
        life_expectancy = float(row[3])

        avg_life = (life_expectancy) / (life_expectancy) 

        chosen_year = ""

        if life_expectancy > max_life:
            max_life = life_expectancy
            max_country = country
        #IF --- FIND MIN_lIFE
                
        #SUM & COUNT VARIABLES NEEDED TO FIND AVERAGE FOR YR OF INTEREST - SHOPPING CART & WORDLE GUIDE
            #FILTER IT BY YEAR BEFORE FINDING AVERAGE (NESTED IF STATEMENTS)

#Tells user to enter year
year_lookup = input("Enter the year of interest: ")

#Generates three expectancy outputs
if chosen_year == year_lookup:
    chosen_year = year_lookup
print(f"For the year: {year_lookup}.\n")
print(f"The average life expectancy across all countries was {avg_life:.2f}\n")
print(f"The max life expectancy was in {max_country} with {max_life:.2f}\n")
print(f"The min life expectancy was in {min_country} with {min_life:.2f}\n")


    #prints the above
print()
print(f"The overall max life expectancy is:{max_life} from {max_country} in {max_year}.\n")
print(f"The overall min life expectancy is:{min_life} from {min_country} in {min_year}.\n")