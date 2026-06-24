screen_time = [568, 626, 573, 246, 180, 645, 160]

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
max_time = max(screen_time)
min_time = min(screen_time)

max_day = days[screen_time.index(max_time)]
min_day = days[screen_time.index(min_time)]

print("Most screen time:", max_day, "-", max_time, "minutes")
print("Least screen time:", min_day, "-", min_time, "minutes")
total = sum(screen_time)
average = total / 7

print("Total weekly screen time:", total, "minutes")
print("Daily average:", round(average, 2), "minutes")


weekdays = screen_time[0:5]
print("Weekday screen times:", weekdays)
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

screen_time = []

for day in days:
    minutes = int(input(f"Enter screen time for {day}: "))
    screen_time.append(minutes)

max_time = max(screen_time)
min_time = min(screen_time)

max_day = days[screen_time.index(max_time)]
min_day = days[screen_time.index(min_time)]

print("\nMost screen time:", max_day, "-", max_time, "minutes")
print("Least screen time:", min_day, "-", min_time, "minutes")

total = sum(screen_time)
average = total / len(screen_time)

print("Total weekly screen time:", total, "minutes")
print("Daily average:", round(average, 2), "minutes")

print("Weekday screen times:", screen_time[0:5])
