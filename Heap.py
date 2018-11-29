class Heap:
 def __init__(self):
    self.heap_array = []
    
 def insert(self, k):
    """
    Appends the value k into the heap array list. After the element has been added
    the heap is then heapified to ensure that the minheap property is mantained.

    Parameters:
        k: value that is to be added to the heap array list
    Returns:
        None
    """  
    self.heap_array.append(k)

    current_index = len(self.heap_array) - 1
    while (current_index > 0):
        parent_index = ((current_index-1)//2)

        if int(self.heap_array[current_index]) > int(self.heap_array[parent_index]): # if no vialation of the min heap property 
            return
        else:   # if heap property is broken then swap the parent and child that are breaking the prop 
            self.heap_array[parent_index], self.heap_array[current_index]  = self.heap_array[current_index], self.heap_array[parent_index]
            current_index = parent_index

 def extract_min(self):
    """
    Removes and returns the smallest element in the heap. The element that is removed is replaced with
    the last element in the heap array. After this swapping, the heap is then heapified so that any violation
    of the minheap properties is remedied.

    Parameters:
        None
    Returns:
        min_elem: the smallest element in the heap (the root)
    """
    if self.is_empty():
        return None
    min_elem = self.heap_array[0]
    aux_elem = self.heap_array.pop()

    if self.is_empty() == False:
        self.heap_array[0] = aux_elem

        current_index = 0
        left_child_index = (2 * current_index) + 1
        current_value = self.heap_array[current_index]

        while left_child_index < len(self.heap_array):  # loop that will repeat until no violation of the minheap properties exist
            current_min = current_value

            for i in range(2): # this loop is in place so that both children are compared and the smaller of the two is chosen 
                if (left_child_index + i) > len(self.heap_array)-1: # condition to avoid out of bounds
                    continue
                else:
                    if int(self.heap_array[left_child_index + i]) < int(current_min): # if child is smaller than parent
                        current_min = self.heap_array[left_child_index + i ]    # set current minimum value
                        current_min_index = left_child_index + i                # and cureent minimim index( index where current minimum value is found )
            if current_min == current_value:    # if no property is broken (in this case, the parent is actually less than its' children)
                break
            else:       # if propert is broken
                self.heap_array[current_index], self.heap_array[current_min_index] = self.heap_array[current_min_index], self.heap_array[current_index] # swap the elements 
                current_index = current_min_index
                left_child_index = int((2 * current_index) + 1)
    return min_elem

 def is_empty(self):
    return len(self.heap_array) == 0
 
 def prints(self):
     """
     prints the contents of the heap array

     Parameters:
        None
     Returns:
        None
     """

     for i in range(len(self.heap_array)):
        print(self.heap_array[i])