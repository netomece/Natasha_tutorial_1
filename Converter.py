class Converter():
    '''
    A class used to convert units of measurement.

    ### Authors
    Person A, Person B, Person C

    # i am person A and B fsdfsdfsfsdf
    '''

    def centimetersToInches(self, centimeter_value):
        # TODO: Person A will implement this method
        return centimeter_value/2.54
    
    def celsiusToFahrenheit(self, celsius_value):
        # TODO: Person B will implement this method
        return (celsius_value * (9/5)) + 32

    def kilogramsToPounds(self, kilogram_value):
        # TODO: Person C will implement this method
        return 0

if __name__ == "__main__":
    my_converter = Converter()
    print("10 centimeters is", my_converter.centimetersToInches(10), "inches.")
    print("10 celsius is", my_converter.celsiusToFahrenheit(10), "fahrenheit.")
    print("10 kilograms is", my_converter.kilogramsToPounds(10), "pounds.")
