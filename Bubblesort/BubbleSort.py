import random 
import time 

def bubblesort (arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if not swapped:
                break

# Run the code. 
# Generate a array of x at a integers at 1 - 100
if  __name__ == "==Main==":
    arr = [random.randint(1,100) for _ in range (1000)]

print ("Ikke sorteret array:", arr)

start = time.time()

bubblesort(arr) 

slut = time.time()
length = slut - start

print ("Sorteret array:")
for num in arr:
        print(num, end="")

print(length, "sekunder")




