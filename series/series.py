from ast import Break


def fibonacci(n):

    if n == 0:
        return 0 

    if n == 1 or n==2:
        return 1

    if n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)
        



def lucas(n):

    if n == 0:
        return 2 

    if n == 1:
        return 1

    if n >= 2:
        return lucas(n-1) + lucas(n-2)






def other_series(n,first_value,second_value):

    if first_value and second_value :

        def custom_series(n):
        
            if n == 0:
                return first_value 

            if n == 1:
                return second_value 

            if n >= 2:
                return  custom_series(n-1) + custom_series(n-2)
        
        return custom_series(n)


def sum_series(n,first_value=0,second_value=1):

   

    if first_value == 0 and second_value == 1 :
        return fibonacci(n)
    
    elif first_value == 2 and second_value == 1 :
        return lucas(n)

  
    else:
        if first_value and second_value :
            return other_series(n,first_value,second_value)        


    





print (sum_series(4,4,4))