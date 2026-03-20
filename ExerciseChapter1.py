"""
Exercise
The following questions give you a chance to practice writing arithmetic expressions:
1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average
pace in seconds per mile?
4. What is your average pace in minutes and seconds per mile?
5. What is your average speed in miles per hour?
"""

Tseconds = int((42*60)+42)
print(f"There are {Tseconds} in 42 minutes 42 seconds")

Tmiles = int((10*1)/1.61)
print(f"There are {Tmiles} in 10km")

AvPa = int(Tseconds/Tmiles)
print(f"Your average pace is {AvPa} seconds per mile")

PaMin = int(AvPa // 60)
PaSec = int(AvPa % 60)
print(f"Your average pace is {PaMin} minutes {PaSec} seconds per mile")

Thour= Tseconds/3600 #No lleva int porque si no, dividiría entre 0 y marca "ZeroDivisionError"
AvSpeed = int(Tmiles/Thour)
print(f"Your average speed is {AvSpeed} miles per hour")









