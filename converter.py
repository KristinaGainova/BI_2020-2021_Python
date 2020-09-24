def Cel_to_Fah(T):
    return T * 1.8 + 32


def Fah_to_Cel(T):
    return (T - 32) / 1.8


def Kel_to_Fah(T):
    return 1.8 * (T - 273) + 32


def Fah_to_Kel(T):
    return (T + 459.67) * (5 / 9)


def Cel_to_Kel(T):
    return Fah_to_Kel(Cel_to_Fah(T))


def Kel_to_Cel(T):
    return Fah_to_Cel(Kel_to_Fah(T))


def Ra_to_Cel(T):
    return (T - 491.67) * 5 / 9


def Cel_to_Ra(T):
    return (T + 273.15) * 9 / 5


def Ra_to_Fah(T):
    return Cel_to_Fah(Ra_to_Cel(T))


def Fah_to_Ra(T):
    return Cel_to_Ra(Fah_to_Cel(T))


def Ra_to_Kel(T):
    return Cel_to_Kel(Ra_to_Cel(T))


def Kel_to_Ra(T):
    return Cel_to_Ra(Kel_to_Cel(T))


def Kel_to_All(T):
    print("%.4f in Kelvins = %.4f in Celsius = "
          "%.4f in Fahrenheit = %.4f in Rankine" %
          (T, Kel_to_Cel(T), Kel_to_Fah(T), Kel_to_Ra(T)))


def Cel_to_All(T):
    print("%.4f in Celsius = %.4f in Kelvins = "
          "%.4f in Fahrenheit = %.4f in Rankine" %
          (T, Cel_to_Kel(T), Cel_to_Fah(T), Cel_to_Ra(T)))


def Fah_to_All(T):
    print("%.4f in Fahrenheit = %.4f in Celsius = "
          "%.4f in Kelvins = %.4f in Rankine" %
          (T, Fah_to_Cel(T), Fah_to_Kel(T), Fah_to_Ra(T)))


def Ra_to_All(T):
    print("%.4f in Rankine = %.4f in Celsius = "
          "%.4f in Fahrenheit = %.4f in Kelvins" %
          (T, Ra_to_Cel(T), Ra_to_Fah(T), Ra_to_Kel(T)))


print("Hello! This is awesome temperature converter!"
      " Please tell me, what temperature of what kind you want to convert!")
print("Supported types: Fahrenheit(F), Rankine(R),"
      " Celsius(C), Kelvin(K). Example: 16 C")
T, type = input().split(' ')
T = float(T)
if type == "R":
    Ra_to_All(T)
elif type == "C":
    Cel_to_All(T)
elif type == "K":
    Kel_to_All(T)
elif type == "F":
    Fah_to_All(T)
else:
    print("Sorry, your type %s is not supported, please try again" % type)
print("Bye!!! Have a nice day!")
