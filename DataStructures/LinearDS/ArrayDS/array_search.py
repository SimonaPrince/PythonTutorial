class ArraySearch:

    def __init__(self):
        pass

    def LinearSearch(self, x, arr):
        for i, key in enumerate(arr):
            if key == x:
                print(f"Value found at pos:{i + 1}")
                break

    # Binary Search using recursive method
    def binarySearch(self, arr, l, r, x):
        mid = (l + r) // 2
        if arr[mid] == x:
            print(f"Array found at pos:{mid}")
        elif mid > x:
            self.binarySearch(arr, l, mid - 1, x)
        elif mid < x:
            self.binarySearch(arr, mid + 1, r, x)


if __name__ == '__main__':
    obj = ArraySearch()
    arr = [34, 56, 21, 67, 98]
    # obj.LinearSearch(21, arr)
    obj.binarySearch(arr, 0, len(arr), 21)
