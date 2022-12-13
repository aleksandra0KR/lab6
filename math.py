def calculate(a, b, operation):
   result = None
   if operation == '+':
       result = a+b
   elif operation == '-':
       result = a-b
   elif operation == '/':
       result = a/b
   elif operation == '*':
       result = a*b
   else:
       print('Неизвестная операция')

   return result
