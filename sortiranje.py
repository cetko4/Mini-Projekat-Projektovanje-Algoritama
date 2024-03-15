popul = 2

def sort(L):
    for i in range(1, len(L)):
        trentuni = L[i]
        j = i - 1
        while j >= 0 and L[j][popul] > trentuni[popul]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = trentuni