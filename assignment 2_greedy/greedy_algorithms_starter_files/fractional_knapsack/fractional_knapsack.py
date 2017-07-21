# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    #print (weights)
    #print (values)
    unit_value = []
    for i in range(len(weights)):
        unit_value.append(values[i]*1.0/weights[i])

    sorted_indices = sorted(range(len(weights)), key=lambda k: unit_value[k], reverse = True)
    #print (sorted_indices)
    
    #while (True):
    for i in sorted_indices:
        if i == len(sorted_indices): # if knapsack has space left even after everything is put inside
            capacity = 0
        if capacity <= 0:
            break
        if weights[i] > 0:
            fraction = min(capacity, weights[i])
            value += fraction*unit_value[i]
            weights[i] -= fraction
            capacity -= fraction
                         
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
