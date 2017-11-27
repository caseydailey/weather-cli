
def weather_report(weather_dict):
    return """
            *****************************
                Your Report is In!!!
            *****************************
                      
            The weather in {} is {} 
            with a temperature of {} and winds of {} mph.

            Suggestions:

            Jacket?  {}
            Umbrella? {}
            Shades? {}

            """.format( weather_dict['city_name'],
                        weather_dict['description'],
                        weather_dict['temp'],
                        weather_dict['wind'],
                        weather_dict['needs_jacket'],
                        weather_dict['needs_umbrella'],
                        weather_dict['needs_shades'])




