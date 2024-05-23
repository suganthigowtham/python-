#Question 1:

list=[10,501,22,37,100,999,87,351]

# Listeven declare  to save Even Numbers 
# Listodd  declare  to save odd numbers
Listeven=[]
Listodd=[]
# Condition to check Even or Odd number
for a in list:
   if(a%2==0):
     Listeven.append(a)
   else:
     Listodd.append(a)

#print the list
print("List1",Listeven)
print("List2",Listodd)


#Question 2:
list=[10,501,22,37,100,999,87,351]

# Declare to save the Prime numbers
Prime=[]
# check and count the prime number
for i in list:
  count=0
  for j in range(1,i):
    if(i%j==0):
      count=+1
  if(count==1):
      Prime.append(i)
print("Prime Number is: ",Prime)


#Question 3:
# To find Happy Numbers
a = [10,501,22,37,100,999,87,351]
b = []
def is_happy(a):
    for i in range (len(a)):
        sum = a[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            b.append(a[i])
    return b
print(is_happy(a))

#Question 4:
#To find the First and Last digit of an Integer
Number=2345
Number=str(Number)
# Storing first and last digit in a variable
First_digit=int(Number[0])
Last_digit=int(Number[-1])
# Adding the variables
Addition=(First_digit+Last_digit)
# Display the result
print(" Addition of first and last digit of an Integer is: ", Number)


#Question 6:

List1=[11,56,34,11,42,86,56,76,34,]
List2=[2,8,9,4,8,2,6]
List3=[21,19,22,10,22]
# Declare to store in list
uniqueList = []
duplicateList = []
 # To find Duplicates in the list
for i in list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)

#Question 7:

#To find the First Non-repeating elements in a list of integers
def firstNonRepeating(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        # if ith element is not present in array except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1
 
 
# Driver code
arr = [2,11,3,2,6,]
n = len(arr)
print(firstNonRepeating(arr, n))


#Question 8:
# To find Minimum element in the Sorted List
Data=[2,5,9,10,4]
#To arrange the list 
Data1=sorted(Data)
print(Data1)
Mim_ele=Data1[0]
print(" The Minimum Element in the list is: ",Mim_ele)

# Question 9:

def find3Numbers(A, arr_size, sum):
 
    # Fix the first element as A[i]
    for i in range( 0, arr_size-2):
 
        # Fix the second element as A[j]
        for j in range(i + 1, arr_size-1): 
             
            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", (A[i], A[j], A[k]))
                    return True
     
    # If we reach here, then no triplet was found
    return False
 
# Driver program to test above function 
A = [10,20,30,9]
sum = 59
arr_size = len(A)
find3Numbers(A, arr_size, sum)

# Question 10:
def subArrayExists(arr, n):
    for i in range(n):
        # Starting point of the subarray and sum is initialized with the first element of subarray
        sum = arr[i]
        if sum == 0:
            return True
        for j in range(i + 1, n):
            # We are finding the sum till the jth index
            # starting from the ith index
            sum += arr[j]
            if sum == 0:
                return True
    return False
 
# Driver's code
if __name__ == "__main__":
    arr = [4,2,-3,1,6]
    N = len(arr)
 
    # Function call
    if subArrayExists(arr, N):
        print("Found a subarray with 0 sum")
    else:
        print("No Such Sub Array Exists!")