import sys

snowballs_count = int(input())
highest_value_snowball = -sys.maxsize
best_weight = 0
best_time = 0
best_quality = 0
for current_snowball in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > highest_value_snowball:
        highest_value_snowball = int(snowball_value)
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality
print(f"{best_weight} : {best_time} = {highest_value_snowball} ({best_quality})")
