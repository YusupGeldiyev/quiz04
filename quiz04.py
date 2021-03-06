def check(vector):
  '''
  this fucntion checks if the given vectors are numbres. if value of the vectors
  equal numbers such as float, int or complex it returns true. othervise it prints 
  "Invalid Input"
  '''
   # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
    else:
      return inputStatus
      
def dot(vector,vector01): 
  '''
  This function takes two vectors (vector01 and vector02) as its arguments. It first checks if two vectors are the same size. 
  If sizes are equal it then takes the dot product of two vectors then returns the result. if not it prints Error and returns none.
    '''
  if check(vector)==True:
    result=0
    a=len(vector)
    b=len(vector01)
    if (a!=b):
  # Here the fucntion checks if two vectors are the same size
      print ("Invalid Input")
      return None
    for i in range(len(vector)):
      result=result+vector[i]*vector01[i]
  # (takes the dot product of two vectors by mulyiplying each  coefficients of two vectors with each other
    return result
  else:
    return "The input is invalid"
  #returns the dot product

vector1=[1,2,2]
vector2=[1,2,3]
vector3=[2,2]
vector4=[1,3,5]
vector6=[1]
vector5=[1,2]
#valid and invalid test values are being checked
#print(dot(vector1,vector2))
#print(dot(vector3,vector4))
#print(dot(vector6,vector5))

def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  if check(vector) == True:
    result = 0
# This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result
  else:
    return "Invalid Input"
vector1=[1,2,2]
vector2=1
#print (twoNorm(vector1))
#print (twoNorm(vector2))

def orthogonVector(vector):
  '''
  This function takes a vector as its argument. it then divides every element of that vector by two norm of that vector. and returns updated orthogonalized vector back
    '''
  if check(vector)==True:
    norm=twoNorm(vector)
  # function that calculates two norm is being assigned
    orthogonalizedVector=[]
  #assigning empty list for new orthog vector
    for i in range(len(vector)):
      newvector=((1/norm))*vector[i]
  #dividing vector values by two  norm
      orthogonalizedVector.append(newvector)
    #returning back to assigned empty
    return orthogonalizedVector
  else:
    return "Invalid Input"
vector1=[1,2,2]
test2=123
#testing valid and not valid inputs
#print(orthogonVector(vector1))
#print(orthogonVector(test2))

def scalarVecMulti(scalar,vector): 
  '''
  This function takes a scalar and a vector as its arguments. Then it multiplies scalar and a vector and returns the updated vector.
  ''' 
 
  if check(vector)==True:
    result=[]
  # creating empty list to return the result after calculation so it puts back a new vector
    for i in range(len(vector)):
      total=0
      total=scalar*vector[i]
  # vector scalar multiplication
      result.append(total)
    return result #returns the new vector
  else:
    return "Invalid Input"
  

# the test values wtih scalar and  different size vectors  are being checked.
scalar=2
vector2=[1,2,3]
vector3=[1,2]
vector4=[1,3,5]
#print(scalarVecMulti(scalar,vector2))
#print(scalarVecMulti(vector3,vector4))

def vecSubtract(vector,vector1): 
  '''
This function takes two vectors (vector01 and vector02) as its arguments. It first checks if two vectors are the same size. 
If sizes are equal it then subtracts vector02 from vector01,then returns the result which is vector. if not it prints Error retruns None".
  '''
  inputStatus = True
  if check(vector)== False:
    inputStatus=False
  if inputStatus== True:
    inputStatus==check(vector1)
  if inputStatus==True:
    result=[]
    # assigning an empty list to get back a new vector after calculations
    a=len(vector)
    b=len(vector1)
    if (a!=b):
   # Here the fucntion checks if two vectors are the same size
      print ("Error")
      return None
    for i in range(len(vector)):
      total=0
      total+=vector[i]-vector1[i]
      # vector subtraction
      result.append(total)
    return result
  #returns the new subtracted vector
  else:
    return "Invalid Input"
vector1=[1,2,5]
vector2=[1,2,3]
vector3=[1,2]
vector4=[1,3,5]
#print(vecSubtract(vector1,vector2))
# the test values wtih right and not right vector sizes are being checked.
#print(vecSubtract(vector3,vector4))

def GST(A):
  '''
  This function takes given matrix A and uses above mentioned functions to calculate
  QR factorization(gram schmidt) of that given matrix. It creates R, Q with all zeroes
  then it computes both matrix arguments and returns it back.
  '''
  #rows of matrix A
  m=len(A[0])
  #columns of matrix A
  n=len(A)
  V=A
  #V are the vectors of A
  #creates empty matrices R and Q
  R=[[0]*n for i in range(n)]
  Q=[[0]*m for i in range(m)]
  for i in range(n):
    #this for loop calculates r11 and q1
    R[i][i]=twoNorm(V[i])
    Q[i]=orthogonVector(V[i])
    for j in range(i+1,n):
      #this for loops computes r12,r22 and q 2
      R[j][i]=dot(Q[i],V[j])
      temp=scalarVecMulti(R[j][i],Q[i])
      V[j]=vecSubtract(V[j],temp)    
  return [Q,R]
Matrix=[[2,2,1],[-2,1,2],[18,0,0]]
print(GST(Matrix))
