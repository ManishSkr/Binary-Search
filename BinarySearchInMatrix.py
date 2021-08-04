"""Here we've given a sorted 2D array and we use binary search to find the key in the 2D array for searching row wise and column 
wise sorted matrix"""

def bsMatrix(arr,key):
    row=len(arr)-1
    col= len(arr[0])-1
    i=0
    j=col
    while(i>=0 and i<=row and j>=0 and j<=col):
        if(arr[i][j]==key):
            return i,j
        elif(arr[i][j]>key):
            j-=1
        elif(arr[i][j]<key):
            i+=1
    return -1

arr=[[10,20,30,40],
     [15,25,35,45],
     [27,29,37,48],
     [32,33,39,50],
     [36,37,40,51]]

key=36
print(bsMatrix(arr,key))



