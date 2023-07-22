class Frac:
  """class for rational numbers implemented as tuples of irreducible fractions, hence immutable"""
  _pool = {} # this dictionary will store the numbers generated so far
  
  from math import gcd
    
  
  def __init__(self,num,den=1):
    if den == 0:
      raise AttributeError('Denominator must not be 0 for a rational number.')
    if (not isinstance(num,int)) or (not isinstance(den,int)):
      raise AttributeError('Numerator and denominator must both be integers.')
    if den < 0: #we will store the denominator as always positive, and the numerator will hold the sign
      num *= -1
      den *= -1
    g = self.gcd(num,den) #reduce the fraction to irreducible
    
    self._num = num // g
    self._den = den // g
    
  @classmethod
  def of(cls,num,den=1):
    """
    object factory, must use this for class to work properly
    requires: num,den are ints or floats
    if num and/or den are floats, they will be converted to a fraction using python's builtin as_integer_ratio() method for floats
    """
    if isinstance(num,float):
      num,denOfNum = num.as_integer_ratio()
      if isinstance(den,int):
        den *= denOfNum
      elif isinstance(den,float):
        numOfDen,den = den.as_integer_ratio()
        num,den = num *den, denOfNum * numOfDen
    elif isinstance(den,float):
      numOfDen,den = den.as_integer_ratio()
      num *= den
      den = numOfDen
    newFrac = cls(num,den) #creates a new, reduced fraction from the input
    key = (newFrac._num,newFrac._den)
    if key not in cls._pool:
      cls._pool[key] = newFrac #checks if this reduced fraction is in the dictionary, if not, adds it
    return cls._pool[key] #returns the reduced fraction
  
  def __repr__(self):
    """
    prints the fraction as '(numerator/denominator)', or just 'numerator' if the denominator is 1,
    to avoid ambiguity in the first case, and reduce parentheses in the second case, in long expressions
    """
    num,den = self._num,self._den
    if den == 1:
      return f'{num}'
    return f'({num}/{den})'
  
  def __add__(self,frac2):
    if type(frac2) in [int,float]:
      frac2 = Frac.of(frac2)
    n1,d1,n2,d2 = self._num,self._den,frac2._num,frac2._den
    return Frac.of(n1*d2 + n2*d1,d1*d2)
  
  def __neg__(self):
    return Frac.of(-self._num,self._den)
  
  def __sub__(self,frac2):
    if type(frac2) in [int,float]:
      frac2 = Frac.of(frac2)
    return self + -frac2
  
  def __mul__(self,frac2):
    if type(frac2) in [int,float]:
      frac2 = Frac.of(frac2)
    n1,d1,n2,d2 = self._num,self._den,frac2._num,frac2._den
    return Frac.of(n1*n2,d1*d2)
  
  def _inv(self):
    if self._num == 0:
      raise ZeroDivisionError("You can't divide by 0!")
    return Frac.of(self._den,self._num)
  
  def __truediv__(self,frac2):
    if type(frac2) in [int,float]:
      frac2 = Frac.of(frac2)
    return self * frac2._inv()
      
  # @classmethod
  # def _floatToFrac(cls,fl):
  #   """
  #   takes a float
  #   returns the reduced fraction that represents that float
  #   using python's builtin .as_integer_ratio() method
  #   """
  #   if not isinstance(fl,float):
  #     raise TypeError("The input must be a float!")
  #   num,den = fl.as_integer_ratio()
  #   return cls.of(num,den)
    
  # def __eq__(self,frac2):
  #   n1,d1,n2,d2 = self._num,self._den,frac2._num,frac2._den
  #   return n1==n2 and d1==d2

  @classmethod
  def sum(cls,*args):
    """requires: args are Frac objects"""
    result = Frac.of(0)
    for arg in args:
      result += arg
    return result
  
  @classmethod
  def product(cls,*args):
    """requires: args are Frac objects"""
    result = Frac.of(1)
    for arg in args:
      result *= arg
    return result