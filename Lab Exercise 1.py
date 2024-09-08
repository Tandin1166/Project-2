# 1 Variable Declaration and Types

a=15
b=12
print(type(a))
print(type(b)) 

# 2 Basic Arithmetic Operations


print (a+b)
print (a-b)
print (a*b)
print (a/b)


# 3 Using Variables and Type Casting

c=a//b
print (c)
print ("type of c", type(c))

c_float = float(c)
print("new value=", type(c_float))

# 4 Working with Strings
message = "The result of a divided by b is:"
message_with_result = message + " " + str(c)
print(message_with_result)

# Using Comparison Operators
if a > b :
    print("true")
else:
    print("false")
if a == b :
    print("True")
else :
    print("false")
