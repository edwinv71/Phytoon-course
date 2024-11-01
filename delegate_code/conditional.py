#if else on one line
#concept:one thing or another;hard choice XOR
temp="cold"
clothing="jumper"if temp == "cold" else "Tshirt"
print(clothing)

#ranges
heart_rate=150
blood_pressure={"diastolic":150,"systolic":100}
if heart_rate<130 and blood_pressure["diastolic"]<130:
    print("Healthy guy")
elif heart_rate<160 and blood_pressure["diastolic"]<160:
    print("rin GP")
else:
    print("go to a&e")
