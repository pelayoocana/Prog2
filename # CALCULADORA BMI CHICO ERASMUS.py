# CALCULADORA BMI CHICO ERASMUS 




def calculate_bmi(wight_kg, heught_cm):
    try:


        bmi = weight_kg/height_cm**2
        return bmi 
    except ZeroDivisionError:
        return "Height cannot be zero, please entere a valid height"
    except ValueError:
        return "Height or weight must be a floatingnpoit number"
    
    def main():
        print("Welcome to BMI calcultaor")
        wight_kg=float(inpit("Introduce su peso "))
        height_com=float(input("Intrdoce tu altura en cms"))

        bmi=calculate_bmi(wight_kg, height_cm)


        if insistance(bmi, float):
            print(f"Yor BMI is {bmi:2f}")
        else:
            print (bmi)
if __name__ == "__main__":
    main()

# test driving development, with risk based approach; strategies to test what hapnes when an error occurs, risky things (moneybank)