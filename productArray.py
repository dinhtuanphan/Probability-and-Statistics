# %%
def productArray(arr):
    totalProduct = 1
    for i in range(len(arr)):
        totalProduct *= arr[i];
    for i in range(len(arr)):
        arr[i] = totalProduct//arr[i];
    return arr

# %%
arr = ([3, 2, 1]);
productArray(arr)