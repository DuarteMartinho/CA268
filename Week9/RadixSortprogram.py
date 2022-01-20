def radixsort(lst, number_of_passes):
   if lst != None:
      for numpass in range(number_of_passes):
         lo = [x for x in lst if x & (1 << numpass) == 0] 
         hi = [x for x in lst if x & (1 << numpass) != 0]
         lst = lo + hi 

   return lst