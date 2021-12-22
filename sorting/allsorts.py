import os

class Sorting:
	def __init__(self,arr):
	    self.arr = arr
	    self.n = len(arr)

	def bubbleSort(self):
	    for i in range(self.n):
	        for j in range(0,self.n-i-1):
	            if self.arr[j] > self.arr[j+1]:
	                self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
	    print("bubbleSort",self.arr)


	def selectionSort(self):
	    for i in range(0,self.n):
	        minIndex = i
	        for j in range(i+1,self.n):
	            if self.arr[j] < self.arr[minIndex]:
	                #print("j,a,min",j,self.arr[j],self.arr[minIndex])
	                minIndex = j
	        #print("arr[i], arr[minIndex] ",arr[i], arr[minIndex] )
	        self.arr[i], self.arr[minIndex] = self.arr[minIndex], self.arr[i]
	        #print(f'array pass {i} : {self.arr}')
	    print("selectionSort",self.arr)


	def quickSort(self):
	    pass

	def mergeSort(self):
	    pass
	def insertionSort(self):
	    temp_arr = []
	    for i in range(0,self.n):
	        temp_arr.append(self.arr[i])





arr = [5,4,3,2,2,1,3,9,6]

#
# #Selection Sort
sortme2 = Sorting(arr.copy())
print("before selection sort",arr)
sortme2.selectionSort()


#Bubble Sort
sortme1 = Sorting(arr.copy())
print("before bubble Sort",arr)
sortme1.bubbleSort()


#insetion Sort
sortme3 = Sorting(arr.copy())
print("before insetion Sort",arr)


print(os.getcwd())





