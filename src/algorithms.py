import timeit
from typing import List, Any, Callable



#Merge Sort(custom)
#Big O Notation: O(n log n)
def merge_sort(data: List[Any], key: Callable) -> List[Any]:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = merge_sort(data[:mid], key)
    right_half = merge_sort(data[mid:], key)

    return _merge(left_half, right_half, key)

# Merge helper
def _merge(left: List[Any], right: List[Any], key: Callable) -> List[Any]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



#Binary Search(custom)
#Big O Notation: O(log n)
def binary_search(data: List[Any], target: Any, key: Callable) -> int:
    left, right = 0, len(data) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = key(data[mid])

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


#Benchmarking
def benchmark_sort(data: list, key: Callable) -> dict:

    custom_time = timeit.timeit(
        lambda: merge_sort(data, key), 
        number=10
    )

    builtin_time = timeit.timeit(
        lambda: sorted(data, key=key),
        number=10
    )
    return {
        'merge_sort': custom_time,
        'builtin_in_sorted': builtin_time
    }

