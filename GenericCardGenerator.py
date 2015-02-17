'''
Created on Aug 28, 2014

@author: e001194
'''
import random
# 
# class RandomCC:
#     
#     def __init__(self):
#        
#        
#     def randominteger(self,lowbound,upbound):
#            self.r=random.randint(lowbound,upbound)
       

class RandomCC:

    def __init__(self,name):
        self.name = name

    def randominteger(self, lbound,ubound):
        return random.randint(lbound,ubound)
        
a=RandomCC('A New Random CC')
print a.randominteger(0, 9)
print a.name


        
        
        
    
