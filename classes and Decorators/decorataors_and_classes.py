## Class without getters and setters
class Celcious:
    def __init__(self, temperature = 0) -> None:
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    # getter method
    def get_temp(self):
        print("Getting value....")
        return self._temperature
    # setter method
    def set_temp(self, value):
        print("Setting value....")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
    # creating property object
    temperature = property(get_temp, set_temp)
    
# create a new object
human = Celcious(37)

# set th temperature
#human.temperature = 37

# get the temp attribute
print(f"Temperature in celcious : {human.temperature}")

# get the fahrenheit method
print(f"Temperature in Fahrenheit : {human.to_fahrenheit()}")
# Check the new constraint 
human.set_temp(-30)
# get the fahrenheit method
print(f"Temperature in Fahrenheit : {human.to_fahrenheit()}")

## Class specific 
print(f"class __dict__ : {human.__dict__}")
#print(f"class __hash__ : {human.__hash__ }")

