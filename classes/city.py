class City:
    def __init__(self,temperature, weather_type, precp_chance, humidity, wind_speed):
        self.temperature = temperature
        self.weather_type =weather_type
        self.precp_chance = precp_chance
        self.humidity = humidity
        self.wind_speed = wind_speed

    def print_summary(self):
        print('''Weather forecast for Gweru  = {} \n
               Temperature: {}\n
               Chance of precipitation: {}%\n
               humidity: {}%\n
               Wind speed: {} km/h\n'''
               .format(self.weather_type,
                       self.temperature,
                       int(self.precp_chance*100),
                       int(self.humidity *100),
                       self.wind_speed))
                       
#creating an obj
Gweru =  City(21, 'Sunny', 0.1, 0.63, 10)
Gweru.print_summary()
