from draw import draw_sort

def countingSort(array, exp1, win):
 
    n = len(array)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (array[i].val / exp1)
        count[int(index % 10)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = (array[i].val / exp1)
        output[count[int(index % 10)] - 1] = array[i].val
        count[int(index % 10)] -= 1
        i -= 1
        
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(array)):
        array[i].val = output[i]
        if exp1 == 100:
            array[i].status ="sorted"
        
        
        if i % 5 == 0:
            draw_sort(array, win)
 
# Method to do Radix Sort
def radix(array, win):

 
    max1 = 0
    for num in array:
        if num.val > max1:
            max1 = num.val
 
    exp = 1
    while max1 // exp > 0:
        countingSort(array, exp, win)
        exp *= 10
        
    return array