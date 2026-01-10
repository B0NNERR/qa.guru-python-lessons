def do_sort(arr):
	i = 0

	while i < len(arr) - 1:
		j = i

		while j < len(arr) - 1:
			if arr[i] > arr[j + 1]:
				arr[i], arr[j + 1] = arr[j + 1], arr[i]
			j += 1

		i += 1
	return arr

arr = [4, 3, 2, 1]
print(do_sort(arr))