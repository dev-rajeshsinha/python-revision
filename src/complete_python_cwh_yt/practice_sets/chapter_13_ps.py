# ----------------------------------------------------------------------------------------------------------------------------------------------

# 1. A Python list contains the multiplication table of 7 from 1 to 10. Write a lambda function to print the multiplication table of 7.

table_of_7 = [7 * i for i in range(1, 11)]
list(map(lambda data: print(f"7 * {data[0]+1} = {data[1]}"), enumerate(table_of_7)))
print()  # Just to add a newline for better readability

# Here, first we have used the `enumerate` function to get both the index and the value as a tuple from the `table_of_7` list. The lambda function takes this tuple as input, deconstructs it into index and value, and prints the multiplication in the desired format. The `map` function applies this lambda function to each element of the enumerated list. One important point to note is that the `map` function returns an iterator, so unless we start consuming it (like converting it to a list or using a loop), the lambda function won't execute. In this case, we have used `list()` to create a list using the iterator created by the `map` function, which forced the execution of the lambda function for each element in the enumerated list, and we can see the output on the console.

# ----------------------------------------------------------------------------------------------------------------------------------------------
