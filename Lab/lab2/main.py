from Fraction import Fraction


def main():
    f1 = Fraction(1,3)
    f2 = Fraction(5,10)

    print(f"Fraction 1: {f1}")
    print(f"Fraction 2: {f2}")

    if f1 > f2:
        print(f"{f1} > {f2}")
    elif f1 == f2:
        print(f"{f1} = {f2}")
    else:
        print(f"{f1} < {f2}")

main()
