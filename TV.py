class TV:
    def __init__(self, brand, price, inches, onoff_status=False, volume=50):
        self.brand = brand
        self.channel = 1  # Default channel
        self.price = price
        self.inches = inches
        self.onoff_status = onoff_status
        self.__volume = volume  # Private member variable for volume

    def __str__(self):
        return f"TV: {self.brand}, Channel: {self.channel}, Price: Rs{self.price}, Inches: {self.inches}, On/Off: {self.onoff_status}, Volume: {self.__volume}"

    def increase_volume(self):
        if self.__volume < 100:
            self.__volume += 1
            print("Volume increased to:", self.__volume)
        else:
            print("Volume is already at maximum (100)")

    def decrease_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
            print("Volume decreased to:", self.__volume)
        else:
            print("Volume is already at minimum (0)")

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
            print("Channel set to:", self.channel)
        else:
            print("Invalid channel number. TV remains on current channel:", self.channel)

    def reset_tv(self):
        self.channel = 1
        self.__volume = 50
        print("TV reset to default settings: Channel 1, Volume 50")

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.__volume}"

# Test the class
my_tv = TV(brand="panasonic", price=99999, inches=55)
print(my_tv)

# Increase volume
my_tv.increase_volume()

# Set channel
my_tv.set_channel(8)

# Print status
print(my_tv.status())

#trying to set 51th channel
my_tv.set_channel(51)

print(my_tv.status())

my_tv.reset_tv()

print("After resetting..")

print(my_tv.status())
