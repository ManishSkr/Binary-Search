"""Here we find how many times a sorted array is rotated. This problem is a variation of binary search
here the logic was we need to find the index of minimum element that gives us the number of rotation in an
array"""

def NoOfRoation(arr):
    return arr.index(min(arr))


arr=[11,12,13,14,2,3,4,5]
print(NoOfRoation(arr))