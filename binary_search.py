def binary_search(data: List[int], target: int) -> int:
    """
    Performs binary search on a sorted list.
    Returns the index of the target, or -1 if not found.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        if data[mid] == target:
            return mid  # Target found
        elif data[mid] < target:
            # Target is in the upper half
            low = mid + 1
        else:
            # Target is in the lower half
            high = mid - 1
            
    return -1 # Target not found

# Example Usage:
# result = binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23)
# print(f"Index: {result}") # Output: Index: 5
