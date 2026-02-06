def print_title(title):
    print()
    print("=" * 30)
    print(f"{title}")


def fibonacci(size=10):
    print_title("FIBONACCI")
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < size:
        next_num = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_num)

    print(f"Size: {size}")
    print(f"Result: {fibonacci_list}")


def find_lowest_number(nums):
    print_title("LOWEST NUMBER")
    # Tidak perlu copy karena kita hanya membaca (read-only)
    lowest_num = nums[0]
    for num in nums:
        lowest_num = num if num <= lowest_num else lowest_num
    print(f"Nums: {nums}")
    print(f"Lowest: {lowest_num}")


def bubble_sort(nums):
    print_title("BUBBLE SORT")
    # Kita copy supaya list asli 'nums' tidak berubah urutannya di luar fungsi
    nums_copy = nums.copy()
    n = len(nums_copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums_copy[j] > nums_copy[j + 1]:
                nums_copy[j], nums_copy[j + 1] = nums_copy[j + 1], nums_copy[j]

    print(f"Original: {nums}")
    print(f"Sorted:   {nums_copy}")
    return nums_copy  # Kita return supaya bisa dipakai di Binary Search


def selection_sort(nums):
    print_title("SELECTION SORT")
    # WAJIB COPY karena ada proses .remove()
    temp_nums = nums.copy()
    sorted_nums = []
    while temp_nums:
        min_num = min(temp_nums)
        sorted_nums.append(min_num)
        temp_nums.remove(min_num)

    print(f"Original: {nums}")
    print(f"Sorted:   {sorted_nums}")


def linear_search(nums, search):
    print_title("LINEAR SEARCH")
    for index, num in enumerate(nums):
        if num == search:
            print(f"Found {search} at index {index}")
            return
    print(f"{search} not found")


def binary_search(nums, search):
    print_title("BINARY SEARCH")
    # Binary search butuh data terurut, kita urutkan salinannya saja
    sorted_nums = sorted(nums.copy())
    print(f"Searching {search} in sorted list: {sorted_nums}")

    left, right = 0, len(sorted_nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_nums[mid] == search:
            print(f"Found {search} at index {mid} (of sorted list)")
            return
        elif sorted_nums[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    print(f"{search} not found")


# --- MAIN PROGRAM ---
nums = [7, 12, 9, 4, 11]

fibonacci(10)
find_lowest_number(nums)
bubble_sort(nums)
selection_sort(nums)
linear_search(nums, 9)
binary_search(nums, 9)
