while True:
    firstdig= int(input('first'))
    b=float
    secdig=int(input('second'))
    oprt=input('operation')
    match oprt:
        case '*':
            print(firstdig*secdig)
            break
        case '+':
            b=firstdig+secdig
            break
        case '-':
            b=firstdig-secdig
            break
        case'/':
            b=firstdig/secdig
            break
        case '√':        
         b=secdig**(1/firstdig)
         if b==int(b):
              b=int(b)
         print(b)
         break
            
            
            
    