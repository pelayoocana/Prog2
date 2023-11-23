# sum of even numbers; 1 to 100 
# highlight the key factors 
# we have to build a technical/diagram before programming 
# all programs ust start with a main function
# draw a flowchat 







def calculation():
    result= 0
    number = 2
    while number <= 100:
        result += number
        number += 2

        print("Sum of even number (Method 2) : ", result)

def main():
    calculation()

if __name__ == "__main__":
    main()