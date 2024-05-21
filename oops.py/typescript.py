#TV-class 

class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 5000 
        self.inches = 24  
        self.volume = 50
        self.on = False  # OnOFF status
    
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
    
    def decrease_volume(self):
        if self.volume > 0:
              self.volume -= 1
    
    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
    
    def reset_tv(self):
        self.channel = 1
        self.volume = 50
    
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

#LED-TV Class
class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0 
        self.backlight = False  
    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} inches\n" \
               f"Energy Usage: {self.energy_usage} W\n" \
               f"Lifespan: {self.lifespan} years\n" \
               f"Refresh Rate: {self.refresh_rate} Hz\n" \
               f"Viewing Angle: {self.viewing_angle} degrees\n" \
               f"Backlight: {'On' if self.backlight else 'Off'}"
 #PART-B   
class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0  
        self.backlight = False  

    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} inches\n" \
               f"Energy Usage: {self.energy_usage} W\n" \
               f"Lifespan: {self.lifespan} years\n" \
               f"Refresh Rate: {self.refresh_rate} Hz\n" \
               f"Viewing Angle: {self.viewing_angle} degrees\n" \
               f"Backlight: {'On' if self.backlight else 'Off'}"



led_tv = LedTV("Sony", 1.5, 150, 5, 120)
led_tv.increase_volume()
led_tv.set_channel(10)
print(led_tv.status())
print(led_tv.display_details())
    





