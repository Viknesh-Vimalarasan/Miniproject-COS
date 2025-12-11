# funktion binary_search (liste, mål):
    # lav = 0
    # høj = længden af liste - 1

    # mens lav <= høj:
        # mid = (lav + høj) // 2
        # hvis liste[mid] == mål:
            # return mid
    # ellers hvis liste[mid] < mål:
        # lav = mid + 1
    # ellers: 
        # høj = mid -1
    # return - 1 # ikke fundet

def binary_searh (list, key):
    low = 0 
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == key:
            return mid 
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return - 1


        