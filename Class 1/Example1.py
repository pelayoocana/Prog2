def func1():

    sum_even= 0
    for i in range(2, 101, 2):
        sum_even += i


    print("Sum of even number", sum_even)

def main():
    func1()

if __name__ == "__main__":
    main()
