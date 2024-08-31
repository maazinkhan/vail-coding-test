def rotate_array(arr, positions):
    # First checking if the positions is a negative number
    if positions < 0:
        raise ValueError("Negative rotation values are not allowed.")
    
    n = len(arr)
    
    # if the user inputs only one digit or an empty array we return back the sanme array
    if n == 0 or n == 1:
        return arr
    
    # ensuring that even if the number of positions is greater than the length of the array, the rotations are handled correctly.
    positions = positions % n
 
    rotated_array = arr[positions:] + arr[:positions]
    
    return rotated_array
