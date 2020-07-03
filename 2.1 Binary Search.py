def partition(arr,low,high): 
	i,j = low+1,high # pivot is the first element
	while(True):
		while arr[i]<=arr[low]:
			if i == high:
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

 
def quickSort(arr,low,high): 
	if low < high: 
		pi = partition(arr,low,high) 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 
		return arr

def quicksort(arr):
	return quickSort(arr,0,len(arr)-1)
 

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))
