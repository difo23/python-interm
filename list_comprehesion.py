def run():
   list_hundred_natural = [x*x for x in range(1,101)]
   list_odd_numbers = [x for x in range(1,101) if x%2 == 0 ]
   print(list_hundred_naturals)
   print(list_odd_numbers)



# List Comprehension:
'''
    [ output  for v in a_lis  condiction]
    They have three parts:
    First is the output, you can use the v in the for.
    Second is the for over v and a list or range.
    Third is the condiction this is optional.
'''




if __name__ == '__main__':
    run()