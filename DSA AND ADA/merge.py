def merge_sort(list):
    list_length = len(list)

    if list_length == 1:
        return list

    q = list_length // 2  # calculate the central point
    left = merge_sort(list[:q])
    right = merge_sort(list[q:])

    return merge(left, right)


def merge(left, right):
    ordered = []

    while left and right:
        ordered.append((left if left[0] <= right[0] else right).pop(0))
    return ordered + left + right


numbers = [10, 5, 12, 1, 9]
print(numbers)
sorted_list = merge_sort(numbers)
print(sorted_list)
