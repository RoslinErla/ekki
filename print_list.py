# Print your list to the screen
# ○ Traverse the list and for each element in the list
# ■ Print the number to the screen
# ■ Make the whole list display in one line
# ■ Separate with both comma and space
# ● 3, 6, 1, 8, 3
# ■ Make sure there is not a comma at the end
# ○ Make a function that does this for you
# ■ The function can take a list as a parameter
# ○ What is the time complexity of this operation?
# ■ Ísl: hver er tímaflækja þessarar aðgerðar?
# ○ Now you can use this function to test all your other list operations, by outputting the
# results
#Time complexity = O(n) liner time in size of list

def print_list(a_list):
    if len(a_list) > 0:
        str_val = str(a_list[0])
    for i in range (1,len(a_list)):
        str_val += ", " + str(a_list[i])
    print(str_val)

a = [1,2,3,4,5]
print_list(a)
