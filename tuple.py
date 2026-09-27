# a = (2,4,5,6,87)

# * tuple is immutable
# b = (3,5,7,8,2, 8364,5,6, "dkhjkjf", False)

# print(type(b))

# no = b.count(5)
# no = b.index(5)
# print(no)

# e = set() //empty set//
# s = {3,5,6,87,5,3,3} // its return only unique value.
# print(s)


# s = {3,4,5,65,6,4,3,3,"mock prepare"}
# s.add(36)
# print(s, type(set))

# Sets Union and Intersection 

# s1 = {2,3,4,5,6,7}
# s2 = {9,9,7,4,5}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print({3,87}.issubset(s1))
# print({3,87}.issuperset(s1))

# n = int(input("enter a number"))

# for i in range(1,11):
#   # print(f"n X i",n*i )
#   print(f"{n} X {i} = {n * i}")


# l = ["ayush", "billionare", "Millionare", "Mock prepare", "Alok"]

# for name in l:
#   if(name.startswith("M")):
#     print(f"MAke a {name}")

# doing while loop

# n = int(input("enter a number"))
# i = 1
# while(i<11):
#   print(f"{n} X {i} = {n * i}")
#   i = i+1


# Find out the number of prime or not

# n = int(input("enter a number : "))

# for i in range(2 , n):
#   if(n%i) == 0 :
#     print("number is not prime")
#     break
#   else:
#     print("number is prime")


# Find the sum of natural number mere bacche

# n = int(input("enter a number : "))
# i = 1
# sum = 0
# while(i <= n):
#   sum +=i
#   i+=1
#   # print("Total number will be :" ,sum) 
#   print(sum)

# Find facorial through for loop

n = int(input("enter a number : "))
multi = 1
for i in range(1 , n+1):
  multi = multi * i
  print(f"product will be", multi)
  