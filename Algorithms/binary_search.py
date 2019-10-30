
# Note that binary searches are only used in sorted arrays
# Searches the input array 'arr' for specified value 'val'
def binary_search(arr, val):

    # if our input is empty or we only have a single element
    # and that element is NOT the value we're searching for,
    # return false
    if len(arr)==0 or (len(arr)==1 and arr[0]!=val):
        return False

    # value at the middle or the array
    mid = arr[int(len(arr)/2)]

    if val==mid: return True
    if val<mid: return binary_search(arr[:int(len(arr)/2)],val)
    if val>mid: return binary_search(arr[int(len(arr)/2+1):],val)


# Testing the binary search
a = [1,2,3,4,5,6,7,8,9,44,45,56]
print(binary_search(a, 10))