def fahrenheit_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]

i = 0

while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_cel(temperature_list[i]), 1)
    print(temperature_list[i])
    i += 1

print("why")
