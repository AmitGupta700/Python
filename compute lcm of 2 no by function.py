def calclcm_(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while 1:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
print("LCM of two numbers is-",calclcm_(int(input("num1:-")),int(input("num2:-"))))
