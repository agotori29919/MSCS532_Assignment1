"""
Commit-3 
Name: Abdul Raheman

Sorts an array in monotonically decreasing order using the Insertion Sort algorithm.  
Args - A (list), The input array to be sorted. 
"""

def insertion_sort(A):
  
    # Begin iterating through the array at the second element (index 1)
    for i in range(1, len(A)):
        # Storing current element as the key
        key = A[i]
        # Initializing the index for the previous element
        j = i - 1
        # Shift elements greater than the key to the right
        while j >= 0 and A[j] < key:
            # Shift the element at index j to the right
            A[j + 1] = A[j]
            # Decrement the index
            j -= 1
        # Insert the key at the correct position
        A[j + 1] = key
    # Return the sorted array
    return A

#Testing with an example below
A = [3, 2, 5, 8, 1, 6, 4]
print("Original array:", A)
sorted_A = insertion_sort(A)
print("Sorted array:", sorted_A)
