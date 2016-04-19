# -*- coding:utf-8 -*-
class Solution:
  	def Fibonacci(self, n):
 		lhm=[[0,1],[1,1]]
  		rhm=[[0],[1]]
  		em=[[1,0],[0,1]]
  		def matrix_mul(lhm,rhm):
  			result=[[0 for i in range(len(rhm[0]))] for j in range(len(rhm))]
  			for i in range(len(lhm)):
 				for j in range(len(rhm[0])):
 					for k in range(len(rhm)):
 						result[i][j]+=lhm[i][k]*rhm[k][j]
 			return result
 		def matrix_square(mat):
 			return matrix_mul(mat,mat)

 		def fib_iter(mat,n):
 			if not n:
 				return em
 			elif(n%2):
 				return matrix_mul(mat,fib_iter(mat,n-1))
                        else:
                                return matrix_square(fib_iter(mat,n/2))
 		return matrix_mul(fib_iter(lhm,n),rhm)[0][0]
a = Solution()
print a.Fibonacci(10)
