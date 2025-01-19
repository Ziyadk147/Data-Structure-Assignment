import csv
def read_weather_data(file_path):
    weather_data = []
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Temperature'] = float(row['temperature(F)'])
            weather_data.append(row)
    return weather_data
def average_temperature_first_week(weather_data):
    first_week_data = weather_data[:7]
    total_temperature = sum(day['Temperature'] for day in first_week_data)
    return total_temperature / len(first_week_data)

def max_temperature_first_10_days(weather_data):
    first_10_days_data = weather_data[:10]  
    return max(day['Temperature'] for day in first_10_days_data)

weather_data = read_weather_data('nyc_weather.csv')


avg_temp_first_week = average_temperature_first_week(weather_data)
max_temp_first_10_days = max_temperature_first_10_days(weather_data)

print(f"Average temperature in first week of January: {avg_temp_first_week:.2f}°C")
print(f"Maximum temperature in first 10 days of January: {max_temp_first_10_days:.2f}°C")
