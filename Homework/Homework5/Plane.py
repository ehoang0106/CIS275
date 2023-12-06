import random
from PriorityQueue import PriorityQueue
from ArrayQueue import ArrayQueue

class Plane:
    def __init__(self, tick):
        self.fuel = random.randint(5, 15)
        self.transaction_time = random.randint(1, 3)
        self.arrival_tick = tick

    def __le__(self, other):
        return self.fuel <= other.fuel


def run_simulation(landing_chance, takeoff_chance, ticks):
    landing_queue = PriorityQueue()
    takeoff_queue = ArrayQueue()
    current_plane = None
    current_plane_is_landing = False
    runway_free_at = -1

    total_takeoff_wait_time = 0
    max_takeoff_wait_time = 0
    total_landing_wait_time = 0
    max_landing_wait_time = 0
    planes_landed = 0
    planes_taken_off = 0
    


    last_processed_landing = False 

    for tick in range(ticks):
        if random.randint(1, 100) <= landing_chance:
            new_plane = Plane(tick)
            landing_queue.add(new_plane)

            #print(f"arrived for landing: Fuel = {new_plane.fuel}, Transaction time = {new_plane.transaction_time}\n")

        if random.randint(1, 100) <= takeoff_chance:
            new_plane = Plane(tick)
            takeoff_queue.add(new_plane)
            #print(f"arrived for takeoff: Fuel = {new_plane.fuel}, Transaction time = {new_plane.transaction_time}\n")


        # if current_plane and tick >= runway_free_at:
        #     current_plane.transaction_time -= 1
        #     if current_plane.transaction_time <= 0:
        #         if current_plane_is_landing:
        #             planes_landed += 1
        #         else:
        #             planes_taken_off += 1
        #         
        #         current_plane = None
        #         current_plane_is_landing = False


        


        if current_plane and tick >= runway_free_at:
            current_plane.transaction_time -= 1
            
            if current_plane.transaction_time <= 0:
                if current_plane_is_landing:
                    planes_landed += 1

                    total_landing_wait_time += tick - current_plane.arrival_tick

                    max_landing_wait_time = max(max_landing_wait_time, tick - current_plane.arrival_tick)

                else:
                    planes_taken_off += 1
                    total_takeoff_wait_time += tick - current_plane.arrival_tick
                    max_takeoff_wait_time = max(max_takeoff_wait_time, tick - current_plane.arrival_tick)

                current_plane = None
                current_plane_is_landing = False


        # if not current_plane:
        #     if not landing_queue.is_empty():
        #         
        #         plane_to_land = landing_queue.peek()
        #         if plane_to_land is None:
        #             continue
        #         current_plane = landing_queue.pop()
        #         current_plane_is_landing = True
        #         runway_free_at = tick + current_plane.transaction_time

        if not current_plane:
            if not landing_queue.is_empty() and not last_processed_landing:
                current_plane = landing_queue.pop()
                current_plane_is_landing = True

                last_processed_landing = True  
                runway_free_at = tick + current_plane.transaction_time

                #print(f"starting land: Fuel = {current_plane.fuel}, Transaction time = {current_plane.transaction_time}\n")


            elif not takeoff_queue.is_empty():

                current_plane = takeoff_queue.pop()
                current_plane_is_landing = False
                
                last_processed_landing = False  
                runway_free_at = tick + current_plane.transaction_time
                #print(f"starting take off: Fuel = {current_plane.fuel}, Transaction time = {current_plane.transaction_time}\n")

    if planes_taken_off > 0:
        avg_takeoff_wait_time = total_takeoff_wait_time / planes_taken_off
    else: 
        avg_takeoff_wait_time = 0

    if planes_landed > 0:
        avg_landing_wait_time = total_landing_wait_time / planes_landed
    else:
        avg_landing_wait_time = 0

    return {
        "What is the average time spent waiting for takeoff?": avg_takeoff_wait_time,
        "What is the average time spent waiting to land?": avg_landing_wait_time,
        "What is the longest time spent waiting for takeoff?": max_takeoff_wait_time,
        "What is the longest time spent waiting to land?": max_landing_wait_time,
        "How many planes total took off?": planes_taken_off,
        "How many planes total landed": planes_landed
        
    }


landing_chance = int(input("Enter landing chance: "))
takeoff_chance = int(input("Enter take off chance: "))
ticks = int(input("Enter number of ticks: "))

results = run_simulation(landing_chance, takeoff_chance, ticks)


for i, j in results.items():
    print(f"{i}: {j}")