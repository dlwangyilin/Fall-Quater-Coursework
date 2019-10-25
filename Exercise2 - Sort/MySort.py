def selectionSort(s):
    """
    :param s: input string[]
    :return: void
    """
    for i in range(len(s)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(s)):
            if s[min_idx] > s[j]:
                min_idx = j
        # the first element
        s[i], s[min_idx] = s[min_idx], s[i]

    return

def insertSort(s):
    # Traverse through 1 to len(arr)
    for i in range(1, len(s)):
        key = s[i]
        j = i - 1
        while j >= 0 and key < s[j]:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = key
    return

def in_place_HeapSort(s):
    # To sink the node at index i.
    # n is size of heap
    def sink(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

            # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

            # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            sink(arr, n, largest)

    n = len(s)
    # Build a maxheap in reverse level order
    for i in range(n, -1, -1):
        sink(s, n, i)

    # Move the largest(top) element to the end of list.
    for i in range(n - 1, 0, -1):
        s[i], s[0] = s[0], s[i]  # swap
        sink(s, i, 0)
    return

def mergeSort(s):
    def __merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

            # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def __helper(arr,l,r):
        if l < r:
            # Same as (l+r)/2, but avoids overflow for
            # large l and h
            m = (l + (r - 1)) // 2

            # Sort first and second halves
            __helper(arr, l, m)
            __helper(arr, m + 1, r)
            __merge(arr, l, m, r)

    l = 0
    r = len(s)-1
    __helper(s,l,r)
    return

def quickSort(s):
    def partition(arr, low, high):
        # Always keep every < pivot item in [low, i] , and enry > pivot item in (i, high]
        i = (low - 1)
        pivot = arr[high]  # pivot

        for j in range(low, high):
            # j is used to travel the arr to find the item <= pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def partition2(arr, low, high):
        pivot = arr[low]  # pivot
        while low<high:
            while low<high and arr[high]>=pivot:
                high -=1
            arr[low] = arr[high]
            while low<high and arr[low]<=pivot:
                low += 1
            arr[high] = arr[low]
        arr[low] = pivot
        return low

    def helper(arr,low,high):
        if low < high:
            # lastpivot is the pivot index for last partition
            lastpivot = partition2(arr, low, high)
            helper(arr, low, lastpivot - 1)
            helper(arr, lastpivot + 1, high)
        else:
            return

    low = 0
    high = len(s)-1
    helper(s, low, high)

if __name__ == "__main__":
    print(__name__)  #前后各两个下划线
    str = ["as","sv","er"]
    print("----------Selection Sort----------")
    a = list(str)
    selectionSort(a)
    print("sorted:", a)
    print("unsorted:", str)
    print("----------Insert Sort-------------")
    b = list(str)
    insertSort(b)
    print("sorted:", b)
    print("unsorted:", str)
    print("--------In Place Heap Sort--------")
    c = list(str)
    in_place_HeapSort(c)
    print("sorted:", c)
    print("unsorted:", str)
    print("------------Merge Sort------------")
    d = list(str)
    mergeSort(d)
    print("sorted:", d)
    print("unsorted:", str)
    print("------------Quick Sort------------")
    e = list(str)
    quickSort(e)
    print("sorted:", e)
    print("unsorted:", str)
