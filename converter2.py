# conversion Celsius in Farenheit
def cnv(celsius):
 
    return str(celsius) + " degrees Celsius  are " + str(float(celsius)* (9/5) + 32 ) + " degrees Farenheit"

celsius = input("Give the temperature in degrees Celcius that you want to convert in Farenheit ")
print (cnv(celsius))
