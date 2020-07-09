# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#  Take this opportunity to think about how you can use functions.
#  Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence.
#  The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibonnaciList(userNumber):
    list = [1, 1]

    for item in list:
        if len(list) < userNumber:
            listNumber = list[-1] + list[-2]
            list.append(listNumber)

    print(list)


def main():
    userNumber = int(
        input("Digit how many numbers do you want in a Fibonnaci list: "))
    if (userNumber == 1):
        fiboList = [1]
        print(fiboList)
        exit()
    elif (userNumber == 2):
        fiboList = [1, 1]
        print(fiboList)
        exit()

    else:
        fibonnaciList(userNumber)


main()
