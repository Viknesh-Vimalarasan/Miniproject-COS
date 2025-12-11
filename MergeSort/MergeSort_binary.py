def merge_sort(numbers):

    # A list with 0 or 1 element is already sorted
    if len(numbers) <= 1:
        return numbers

    # Finder midten og splitter det i to
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    # Kalder den rekursivt for at sortere elementerne
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Vi merge de 2 sorterede halvdele sammen
    return merge(sorted_left, sorted_right)

def merge(left, right):

    merged_list = []
    i = j = 0

    # Vi sammen ligner fra begge "lister" og tilføjer altid det mindste hver gang
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # Hvis det er nogle overskydende tal (Hvis det er ikke er et lige antal numre)
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list

values = [
    54, 23, 87, 12, 77, 9, 43, 66, 31, 2,
    90, 28, 19, 50, 71, 4, 39, 15, 99, 1
]

print("Unsorted list:", values)
sorted_values = merge_sort(values)
print("Sorted list:  ", sorted_values)

# Den har Big O: O(n log n) hvilket gør den langt mere effektiv end f.eks bubblesort. Her er 1000 elementer = 10.000 operationer hvor i bubble sort er 1000^2 = 1.000.000 operationer

#Binary search=

def binary_search(lst, key):
    if len(lst) == 0:
        return False  # Key findes ikke i listen

    mid = len(lst) // 2
    middle_value = lst[mid]

    if key == middle_value:
        return True

    elif key > middle_value:
        # Søg i højre halvdel
        return binary_search(lst[mid + 1:], key)

    else:
        # Søg i venstre halvdel
        return binary_search(lst[:mid], key)

try:
    search_for = int(input("Indtast tallet du vil søge efter: "))
except ValueError:
    print("Du skal indtaste et gyldigt heltal!")
    exit()

# Kald binary search
found = binary_search(sorted_values, search_for)

# Print resultat
if found:
    print(f"Tallet {search_for} blev fundet i listen.")
else:
    print(f"Tallet {search_for} findes ikke i listen.")
