# conversion pa / mbar / atm / psi
# mbar = pa / 100
# atm = pa / 101325
# psi = pa / 6895

def multi_cnv_pression_pa(val):
    start_txt = "The convertion of " + str(val) + " pa in mbar/atm/psi = "
    mbar_txt = ",   " + str(val/100) + " mbar"
    atm_txt = ",   " + str(val/101325) + " atm"
    psi_txt = ",   " + str(val/6895) + " psi"
    
    return start_txt + mbar_txt + atm_txt + psi_txt

def multi_cnv_pression_mbar(val):
    start_txt = "The convertion of " + str(val) + " pa in pa/atm/psi = "
    pa_txt = ",   " + str(val*100) + " pa"
    atm_txt = ",   " + str(val/1013.25) + " atm"
    psi_txt = ",   " + str(val/68.948) + " psi"
    
    return start_txt + pa_txt + atm_txt + psi_txt

def multi_cnv_pression_atm(val):
    start_txt = "The convertion of " + str(val) + " pa in pa/mbar/psi = "
    pa_txt = ",   " + str(val*101325) + " pa"
    mbar_txt = ",   " + str(val*1013.25) + " mbar"
    psi_txt = ",   " + str(val*14.6959) + " psi"
    
    return start_txt + pa_txt + mbar_txt + psi_txt

def multi_cnv_pression_psi(val):
    start_txt = "The convertion of " + str(val) + " pa in pa/mbar/atm = "
    pa_txt = ",   " + str(val*6894.76) + " pa"
    mbar_txt = ",   " + str(val*68.9476) + " mbar"
    atm_txt = ",   " + str(val/14.696) + " atm"
    
    return start_txt + pa_txt + mbar_txt + atm_txt

unit = input("Give the unit of the value in pa or mbar or atm or psi: ")
value = input("Give me the pressure in unit selected that you will to convert : ")

if (unit == "pa"):
    print("conversion pa in mbar/atm/psi ")
    print(multi_cnv_pression_pa(float(value)))

if (unit == "mbar"):
    print("conversion mbar in pa/atm/psi ")
    print(multi_cnv_pression_mbar(float(value)))

if (unit == "atm"):
    print("conversion atm in pa/mbar/psi ")
    print(multi_cnv_pression_atm(float(value)))

if (unit == "psi"):
    print("conversion psi in pa/mbar/atm ")
    print(multi_cnv_pression_psi(float(value)))

if (float(value)<50):
    print("The pression is to low")
if (float(value)>500):
    print("The pression is to high")

#print(multi_cnv_pression_pa(float(value)))
