name = ["User1", "User2", "User3", "User4", "User5"]
print("Enter a name to search for")
search = input()
found = False
while not found:
    for i in range(len(name)):
        if name[i] == search:
            found = True
            print("Hello", search, "you have been found")
            break
    else:
        print("Sorry", search, "you have not been found")
        print("Please enter another name to search for:")
        search = input()
# This is a tool to search for a name in a list
# This tool will state you're not found if the name is not in the list
# Other idea to implement would be to use a while loop to keep asking the user for a name until they have found it
