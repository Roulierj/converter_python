# conversion pa / mbar / atm / psi

def multi_cnv_pression(val,unit):

    if(unit == "pa"):
        start_txt = "The convertion of " + str(val) + " pa in mbar/atm/psi = "
        pa_txt = ""
        mbar_txt = ",   " + str(val/100) + " mbar"
        atm_txt = ",   " + str(val/101325) + " atm"
        psi_txt = ",   " + str(val/6895) + " psi"

    if(unit == "mbar"):
        start_txt = "The convertion of " + str(val) + " pa in pa/atm/psi = "
        pa_txt = ",   " + str(val*100) + " pa"
        mbar_txt =""
        atm_txt = ",   " + str(val/1013.25) + " atm"
        psi_txt = ",   " + str(val/68.948) + " psi"
    
   
    if(unit == "atm"):
        start_txt = "The convertion of " + str(val) + " pa in pa/mbar/psi = "
        pa_txt = ",   " + str(val*101325) + " pa"
        mbar_txt = ",   " + str(val*1013.25) + " mbar"
        atm_txt =""
        psi_txt = ",   " + str(val*14.6959) + " psi"
    
    if(unit == "psi"):
        start_txt = "The convertion of " + str(val) + " pa in pa/mbar/atm = "
        pa_txt = ",   " + str(val*6894.76) + " pa"
        mbar_txt = ",   " + str(val*68.9476) + " mbar"
        atm_txt = ",   " + str(val/14.696) + " atm"
        psi_txt = ""
    
    return start_txt + pa_txt + mbar_txt + atm_txt + psi_txt

print("Small routine to convert pression pa/mbar/atm/psi")

unit = input("Give the unit of pression to convert: ")
value = input("Give the value of pression: ")

print(multi_cnv_pression(float(value),unit))

again = input("Would you convert a new value? Yes or No : " )
if(again == "Yes" ):
    print("Ok lets try again")
if(again== "No"):
    print("Program terminated , see you soon")
