add = lambda x, y: x + y
print(add(5, 3))   # 8

# Higher-order function
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
print(doubled)  
