import heapq


def min_cost_to_connect_cables(cables):
    # Transform the list into a min-heap
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Remove and return the smallest element
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Cost of connection
        current_cost = first + second
        total_cost += current_cost

        # Push combined cable back into heap
        heapq.heappush(cables, current_cost)

    return total_cost


# Test
cables1 = [3]
cables2 = [2, 5, 7]
cables3 = [5, 3, 7, 11]
total_min_cost = min_cost_to_connect_cables(cables3)

print(min_cost_to_connect_cables(cables1))
print(min_cost_to_connect_cables(cables2))
print(f"The minimal cost to combine cables is: {total_min_cost}")
