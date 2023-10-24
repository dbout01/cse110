#CALC & RETURN WIND CHILL BASED ON TEMP & WIND SPEED
def wind_chill(temperature, wind_speed):
    wc = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16 #(see formula online)
    return wc

#CONVERTS FROM CELSIUS TO FARENHEIT
def celsius(temperature):
    temp = temperature * (9/5) + 32
    return temp

#USER ENTERS TEMP & CONVERT
temperature = float(input(f'What is the temperature?: '))
forc = input(f'Fahrenheit or Celsius (F/C)?: ')

if forc == 'c':
    temperature = celsius(temperature)


#LOOP & CALCULATE & DISPLAY WIND CHILL
for wind_speed in range(5, 61, 5):
    print(f'At temperature {temperature}F, and wind speed {wind_speed}mph, the windchill is: {wind_chill(temperature, wind_speed):.2f}F')