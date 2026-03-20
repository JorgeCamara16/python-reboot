#How many seconds are there in 42 minutes 42 seconds?
Tseconds = int((42*60)+42)
print(f"There are {Tseconds} seconds in 42 minutes 42 seconds")

#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
miles = int(10/1.61)
print(f"There are {miles} miles in 10 kilometers")

#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
pace = int(Tseconds/miles)
print(f"Your average pace is {pace} seconds per mile")

# What is your average pace in minutes and seconds per mile?
pace_minutes = int(pace // 60)
pace_seconds = int(pace % 60)
print(f"Your average pace is {pace_minutes} minutes and {pace_seconds} seconds per mile")

#What is your average speed in miles per hour?
hours = Tseconds / 3600
speed = int(miles / hours)
print(f"Your average speed is {speed} miles per hour")

