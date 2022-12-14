def calc(operation):
   operation = list(operation.split())
   a = int(operation[0])
   b = int(operation[2])
   ans = "wrong"
   if operation == '+':
       ans = a+b
   elif operation == '-':
       ans = a-b
   elif operation == '/':
       ans = a/b
   elif operation == '*':
       ans = a*b

   return ans

if __name__ == "__main__":
   operation = input()
   print(calc(operation))
