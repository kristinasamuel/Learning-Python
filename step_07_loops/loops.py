#  10 questions 
# count positive numbers how many 

numbers =[1,-2,3,-4,5,6,-7,-8,-9,10]
positive_numbers = 0 
for num in numbers:
    if num > 0:
        positive_numbers += 1
print(f"positive numbers final count : {positive_numbers} ")        


   # sum of even numbers

n = 10 
sum_even = 0
for i in range(1,n+1):
    if i% 2 == 0:
        sum_even +=1
print("sum of even number is:",sum_even)        


 # print a multiplcation tabke  iteratioon 5 

number = 7
for i in range(1,11):
    if i == 5:
        continue
    print(number,"x" , i , "=" ,number * i)

# reverse string using a string

name_str = "python"
reversed_str = ""

for char in name_str:
    reversed_str = char + reversed_str
print(f"reversed string : {reversed_str}")    


