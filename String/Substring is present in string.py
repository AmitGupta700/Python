def check(string, sub_string):
    if (string.find(sub_string) == -1):
        print("No")
    else:
        print("Yes")

string= input("Enter the string")
sub_string= input("Enter The sub-string")
check(string, sub_string)