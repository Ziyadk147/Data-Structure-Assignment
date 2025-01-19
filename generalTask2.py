import csv
def read_weather_data(file_path):
    weather_data = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Temperature'] = float(row['temperature(F)'])
            weather_data.append(row)
    return weather_data

weather_data = read_weather_data('nyc_weather.csv')

def temperature_on_jan_9(weather_data):
    for day in weather_data:
        if day['date'] == 'Jan 9':
            return day['Temperature']

def temperature_on_jan_4(weather_data):
    for day in weather_data:
        if day['date'] == 'Jan 4': 
            return day['Temperature']

temp_jan_9 = temperature_on_jan_9(weather_data)
temp_jan_4 = temperature_on_jan_4(weather_data)

print(f"Temperature on Jan 9: {temp_jan_9:.2f}°C")
print(f"Temperature on Jan 4: {temp_jan_4:.2f}°C")