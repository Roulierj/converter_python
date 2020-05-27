# conversion pa en mbar / atm / psi
# mbar = pa / 100
# atm = pa / 101325
# psi = pa / 6895

def multi_cnv_pression_pa(val_pa):
    start_txt = " the convertion of " + str(val_pa) + " pa in mbar/atm/psi = "
    mbar_txt = ",   " + str(val_pa/100) + " mbar"
    atm_txt = ",   " + str(val_pa/101325) + " atm"
    psi_txt = ",   " + str(val_pa/6895) + " psi"
    
    return start_txt + mbar_txt + atm_txt + psi_txt

print ("Give me the prssure in pa that you will convert in mbar/atm/psi: ")
pa = input()
if (float(pa)<50):
    print("The pression is to low")
if (float(pa)>500):
    print("The pression is to high")

print(multi_cnv_pression_pa(float(pa)))
