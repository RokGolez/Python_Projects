import random
import time

operators = ["+","-","*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression) # eval is used instead of if - else statement
    return expression, answer

wrong = 0
input("Press enter to start ")
print("----------")

start_time = time.time() # Time stamp in seconds


for i in range(total_problems):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expression + "= ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("----------")
print("Well done, you finished in",round(total_time,2),"seconds.")

