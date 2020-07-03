
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	i,j = low+1,high
	while(True):
		while arr[i]<=arr[low]:
			if i == 	high:
				break
			i+=1
		while arr[low]<= arr[j]:
			if j==low:
				break
			j-=1
		if i>=j:
			break
		arr[i],arr[j]=arr[j],arr[i]
	arr[low],arr[j] = arr[j],arr[low]
	return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 
		pi = partition(arr,low,high) 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 
		return arr

def quicksort(arr):
	return quickSort(arr,0,len(arr)-1)
# This code is contributed by Mohit Kumra 

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))