print("Welcome to the Miles Per Hour to Metres Per Second Converter")

#user input to get miles per hour value
mph = float(input("\nEnter the speed in mph you wish to convert to mps: "))

mps = mph*0.4474
#rounds mps calcaluation to 2 decimal places
mps = round(mps,2)

print("\nYour speed in metres per second is " + str(mps) + ".")