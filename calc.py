def calc(operation):
   operation = list(operation.split())
   a = int(operation[0])
   b = int(operation[2])
   ans = "wrong"
   operator = operation[1]
   if operator == '+':
       ans = a+b
   elif operator == '-':
       ans = a-b
   elif operator == '/':
       ans = a/b
   elif operator == '*':
       ans = a*b

   return ans

if __name__ == "__main__":
   operation = input()
   print(calc(operation))
