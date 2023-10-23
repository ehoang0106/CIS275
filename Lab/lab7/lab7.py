from TheaterSimulator import TheaterSimulator


def main():
    length = int(input("Enter clock ticks for simulation:  "))
    odds = float(input("Enter odds of a new customer(between 0 and 1): "))

    for num_cashiers in [1,2,3]:
        print(f"\nSimulation with {num_cashiers} cashiers...")
        t = TheaterSimulator(length, odds, num_cashiers)
        t.run_simulation()
        print("-----------------------")


main()