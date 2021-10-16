while True:
    n=int(input('ENTER A NUMBER TO CHECK DIVISIBILITY: '))
    for i in range (2,n):
        if n%i == 0:
            print('THE ENTER NO. IS DIVISIBLE BY: ',i)
        
