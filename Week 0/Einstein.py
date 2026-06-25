def main():
    mass = float(input("Enter you mass (in Kilogram) "))

    ans = sum(mass)

    print (int(ans))


def sum(mass):

    ans = mass * (300000000 ** 2)

    return ans

main()
