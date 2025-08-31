array = [10, 30, 30, 40, 50]

def sum_arr(arr):
    x = 0
    for i in arr:
        x += i
    return x
    
def largest_element(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
            
    return maximum
    
def smallest_element(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
            
    return minimum
    
def index_of_element(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
            
def multi_index_founder(arr,arr_val):
    idx = []
    for i in arr_val:
        for j in range(len(arr)):
            if i == arr[j]:
                idx.append(j)
    
    return idx
    
def reverse_array(arr):
    x = []
    for i in range(len(arr)):
        i += 1
        x.append(arr[-i])
    return x
    
def is_array_sorted_asc(arr):
    for i in range(len(arr)):
        first = i
        last = i + 1 if i < (len(arr) - 1) else len(arr) - 1
        print(first," ",last)
        if arr[first] > arr[last]:
            return False
    return True
            
def duplicate_val(arr):
    dup = []
    n = len(arr)
    for i in range(n):
        # check if arr[i] appears again later
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                # ensure we only add it once
                already = False
                for v in dup:
                    if v == arr[i]:
                        already = True
                        break
                if not already:
                    dup.append(arr[i])
                break  # move to next i after first repeat found
    return dup

    
print(duplicate_val(array))