import numpy as np

x = np.random.randint(20, size=15)      # use numpy to generate a random vector of size 15 (0-20 range of integers)

def most_frequent_item(x):

    count = {}
    max_count = 0
    max_item = None

    for i in x:
        if i not in count:
            count[i] = 1

        else:
            count[i] += 1       # if we see the number again, then we add +1 to count

        if count[i] > max_count:    # updates the maximum count if i > max_count
            max_count = count[i]
            max_item = i            # current max number is updated

    return max_item

print("Randomly generated vector list:", x)
print("The number that appears the most is:", most_frequent_item(x))



