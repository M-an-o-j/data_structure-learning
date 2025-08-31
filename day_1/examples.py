arr = [1,2,3,4,5,6]

def last_element(arr):
    return arr[-1]

def maximum_element(arr):
    return max(arr)

def alternative_max_element(arr):
    maximum = arr[0]
    for x in arr:
        if x > maximum:
            maximum = x
    return maximum


def print_all_pair(arr):
    for i in arr:
        for j in arr:
            print(i, j)


#two sum
def two_sum(arr, target):
    for i in arr:
        for j in arr:
            if (i+j) == target:
                return [i,j]
            
print(two_sum([2,7,11,15],4))

def alternate_two_sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):  # avoid same element twice
            if arr[i] + arr[j] == target:
                return [i, j]    # return indices
    return []

#buy and sell stock
def buy_and_sell_stock(arr):
    maximum = arr[0]
    minimum = arr[0]

    for i in arr:
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i
    
    return [minimum, maximum]

print(buy_and_sell_stock([7,1,5,3,6,4]))

def alternative_buy_and_sell_stock(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)  # track min so far
        profit = price - min_price         # profit if sold today
        max_profit = max(max_profit, profit)
    
    return max_profit
