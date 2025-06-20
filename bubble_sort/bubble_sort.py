def bubble_sort(data):
        n = len(data)
        for i in range(n):
        
            for j in range(0, n - i - 1):
            
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
data= [5, 3, 2, 4, 4, 1]
sorted_array = bubble_sort(data)
print("Sorted array is:", sorted_array)

    
        
    
 
