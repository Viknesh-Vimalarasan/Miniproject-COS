import time

value = [1,3,5,6,8,12,44]
key_to_get = 22

def linear_search(list, key):
    for i in range(len(list)):
        if list[i] == key:
            return i 
    return -1

start_time = time.time()
result = linear_search(value, key_to_get)
end_time = time.time()

print(f"Key {key_to_get} found at index {result} it took {end_time - start_time:.8f} secounds")
