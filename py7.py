
temperatures = [28, 32, 31, 35, 30, 29, 33]


hottest = max(temperatures)
coldest = min(temperatures)
print(f"Hottest Temperature: {hottest}°C")
print(f"Coldest Temperature: {coldest}°C")


average_temp = sum(temperatures) / len(temperatures)
above_average_days = [temp for temp in temperatures if temp > average_temp]
print(f"Average Temperature: {average_temp:.2f}°C")
print(f"Days above average: {len(above_average_days)}")


print("First 3 days' temperatures:", temperatures[:3])
print("Last 2 days' temperatures:", temperatures[-2:])
