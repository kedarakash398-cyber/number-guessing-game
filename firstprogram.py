
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1,100)

print("welcome to the number guessing game!")
print("i'm thinking of a number between 1 and 100")

attempts = 0

while True:
    guess =int(input("enter your guess:"))
    attempts +=1
    
    if guess< secret_number:
        print("Too low! try again.")
    elif guess> secret_number:
        print("Too high! try again.")   
    else:
        print(f" congratulations! you guessed the number in {attempts} attempts")
        break
    
        
        
        
    
    
   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
      
 
    
    
        
        
        
        



