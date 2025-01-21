# **************************************************************************

TEST_MODE = False

TEST_TEMPERATURE = 54.2

TEST_WIND_SPEED = 13.1

# **************************************************************************

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + (0.6215 * temperature) - (35.75 * pow(wind_speed, 0.16)) + (0.4275 * temperature * pow(wind_speed, 0.16))

# **************************************************************************

print('This program computes wind chill in Fahrenheit.')

temperature = TEST_TEMPERATURE if TEST_MODE else float(input('Enter the current temperature in degrees F: '))
wind_speed = TEST_WIND_SPEED if TEST_MODE else float(input('Enter the current wind speed in miles/hour: '))

wind_chill = calculate_wind_chill(temperature, wind_speed)

print('\nWhen the temp is ' + str(temperature) + ' and wind speed is ' + str(wind_speed) + ', the wind chill in F is ' + str(round(wind_chill,1)))

# **************************************************************************