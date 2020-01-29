# ● Binary search
# ○ Implement binary search in an ordered list using recursive programming

def binary_search(a_list,value,left, right):
    if a_list == []:
        return False

    mid = left + (right-1) // 2

    
    if a_list[mid] == value:
        return mid

    if a_list[mid] < value:
        return binary_search(a_list,value,mid +1 , right)

    if a_list[mid] > value:
        return binary_search(a_list,value,left,mid - 1)

a_list = [1,2,4,6,8,9]
length = len(a_list) -1 

print(binary_search(a_list,8,0, length))