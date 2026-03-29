class Solution:
    # Function to merge two halves
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low, mid + 1

        # Merge both sorted halves
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining left elements
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining right elements
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted temp into original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Recursive merge sort
    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)


# Driver code
arr = [5, 2, 8, 4, 1]
sol = Solution()
sol.mergeSort(arr, 0, len(arr) - 1)
print(*arr)


def merge_sort(arr):
    # Base case: if array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from both arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements (if any)
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)

print("Original array:", arr)
print("Sorted array:", sorted_arr)