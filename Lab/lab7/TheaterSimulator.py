from Cashier import Cashier
from Customer import Customer


class TheaterSimulator:
    def __init__(self, length, odds_of_new_customer, num_cashiers):
        self._odds_of_new_customer = odds_of_new_customer
        self._simulation_length = length
        self._cashier = []

        for i in range(num_cashiers):
            self._cashier.append(Cashier())

    # def run_simulation(self):
    #     """ Run the simulation for self._simulation_length clock ticks """
    #     for cur_time in range(self._simulation_length):
    #         # Attempt to generate a new customer each clock tick
    #         new_customer = Customer.generate_customer(self._odds_of_new_customer, cur_time)

    #         if new_customer is not None:
    #             self._cashier.add_customer(new_customer)

    #         self._cashier.serve_customer(cur_time)

    #     self._cashier.print_statistics()

    def run_simulation(self):
        for cur_time in range(self._simulation_length):
            new_customer = Customer.generate_customer(self._odds_of_new_customer, cur_time)


            if new_customer:
                shortest_queue_length = len(self._cashier[0]._queue)
                shortest_queue_cashier = self._cashier[0]

                for cashier in self._cashier[1:]:
                    if len(cashier._queue) < shortest_queue_length:
                        shortest_queue_length = len(cashier._queue)
                        shortest_queue_cashier = cashier


                shortest_queue_cashier.add_customer(new_customer)
            
            for cashier in self._cashier:
                cashier.serve_customer(cur_time)

        
        for i, cashier in enumerate(self._cashier, 1):
            print(f"\nCashier {i} Statictics: ")
            cashier.print_statistics()