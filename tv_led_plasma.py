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

class LEDTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate,
                 onoff_status=False, volume=50):
        super().__init__(brand, price, inches, onoff_status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return f"{self.brand} has a wider viewing angle for immersive viewing experience."

    def backlight(self):
        return f"{self.brand} uses advanced backlight technology for better contrast and brightness."

    def display_details(self):
        details = f"Brand: {self.brand}\nPrice: Rs{self.price}\nInches: {self.inches}\nScreen Thickness: {self.screen_thickness}\nEnergy Usage: {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate} Hz"
        return details

class PLASMATV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate,
                 onoff_status=False, volume=50):
        super().__init__(brand, price, inches, onoff_status, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return f"{self.brand} has a wide viewing angle for immersive viewing experience."

    def backlight(self):
        return f"{self.brand} uses backlight technology for better contrast and brightness."

    def display_details(self):
        details = f"Brand: {self.brand}\nPrice: Rs{self.price}\nInches: {self.inches}\nScreen Thickness: {self.screen_thickness}\nEnergy Usage: {self.energy_usage}\nLifespan: {self.lifespan}\nRefresh Rate: {self.refresh_rate} Hz"
        return details

# Creating led tv object and testing it's functionalities
my_led_tv = LEDTV(brand="Sony", price=999, inches=65, screen_thickness="Ultra-thin",
                      energy_usage="Low", lifespan="10 years", refresh_rate=120)
print(my_led_tv)

# Test the additional functionalities
print(my_led_tv.viewing_angle())
print(my_led_tv.backlight())

# Display detailed features
print(my_led_tv.display_details())

my_led_tv.increase_volume()

# Set channel
my_led_tv.set_channel(8)

# Print status
print(my_led_tv.status())

#trying to set 51th channel
my_led_tv.set_channel(51)

print(my_led_tv.status())

my_led_tv.reset_tv()

print("After resetting led tv settings..")

print(my_led_tv.status())


#Creating plasma tv object and testing it's functionalities

my_plasma_tv = PLASMATV(brand="Samsung", price=699, inches=55, screen_thickness="Thin",
                      energy_usage="Low", lifespan="5 years", refresh_rate=100)
print(my_plasma_tv)

# Test the additional functionalities
print(my_plasma_tv.viewing_angle())
print(my_plasma_tv.backlight())

# Display detailed features
print(my_plasma_tv.display_details())

my_plasma_tv.increase_volume()

# Set channel
my_plasma_tv.set_channel(18)

# Print status
print(my_plasma_tv.status())

#trying to set 0th channel
my_plasma_tv.set_channel(0)

print(my_plasma_tv.status())

my_plasma_tv.reset_tv()

print("After resetting plasma tv settings..")

print(my_plasma_tv.status())
