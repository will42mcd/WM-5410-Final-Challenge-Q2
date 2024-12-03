import numpy as np

def create_grid(user_start, user_stop, grid_size):
    array = np.zeros(grid_size, dtype = int, order = 'C')
    row_start = 1
    if user_start == 'TL':
        array_fill = 1
        for i, row in enumerate(array):
            array_fill = row_start
            for j in enumerate(row):
                if array_fill > user_stop:  
                    break
                array[i,j] = array_fill
                array_fill += 1
            row_start += 1
        print(array)

    elif user_start == 'TR':
        print("TR")
        array_fill = 1
        for i, row in enumerate(array):
            array_fill = row_start
            for j in range(len(array[i])-1, -1, -1):
                if array_fill > user_stop:  
                    break
                array[i,j] = array_fill
                array_fill += 1
            row_start += 1
        print(array)

    elif user_start == 'BL':
        print("BL")
        for i in range(len(array)-1, -1, -1):  
            array_fill = row_start
            for j in range(len(array[i])): 
                if array_fill > user_stop:  
                    break 
                array[i, j] = array_fill  
                array_fill += 1  
            row_start += 1   
        print(array)           
        
    elif user_start == 'BR':
        print("BR")
        for i in range(len(array)-1, -1, -1):  
            array_fill = row_start
            for j in range(len(array[i])-1, -1, -1):
                if array_fill > user_stop:  
                    break  
                array[i, j] = array_fill  
                array_fill += 1  
            row_start += 1  
        print(array)