# max_num

def max_num(one,two,three):
  return max([one,two,three])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

#  mult_list  

def mult_list(one):
  if len(one) == 0:
    return 0

  num = one[0]

  if len(one) > 1:
    for i in one[1:]:
      num = num * i

  return num
    
print(mult_list([5,10,15]))


# rev_string() 

def rev_string(str):
  return str[::-1]


print(rev_string("John"))


#  num_within() 

def num_within(a,b,c):
  return a in range(b,c+1)
     
print(num_within(1,2,3))     


#  pascal() 

triangle = [[1],[1,1]]
def pascal(n):

  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)

pascal(2)
