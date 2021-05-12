class Converter():
    '''
    A class used to convert units of measurement.

    ### Authors
    Person A, Person B, Person C
    '''

    def centimetersToInches(self, centimeter_value):
        return centimeter_value/2.54
    
    def celsiusToFahrenheit(self, celsius_value):
        return (celsius_value * (9/5)) + 32

    def kilogramsToPounds(self, kilogram_value):
        return kilogram_value * 2.205

    def dollarsToNickels(self, dollar_value):
        return dollar_value * 20
        
    def milesToKilometers(self, miles_value):
        return miles_value * 1.60934
        
    def weeksToSeconds(self, weeks_value):
        return weeks_value * 604800

if __name__ == "__main__":
    my_converter = Converter()
    print("10 centimeters is", my_converter.centimetersToInches(10), "inches.")
    print("10 celsius is", my_converter.celsiusToFahrenheit(10), "fahrenheit.")
    print("10 kilograms is", my_converter.kilogramsToPounds(10), "pounds.")
    print("10 dollars is", my_converter.dollarsToNickels(10), "nickels.")
    print("10 miles is", my_converter.milesToKilometers(10), "kilometers.")
    print("10 weeks is", my_converter.weeksToSeconds(10), "seconds.")
