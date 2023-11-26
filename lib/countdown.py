# your code goes here!
import time

# !user interactive program
# count = int(input("Enter count: "))

def countdown(count):  
    # count still positive
    while count > 0:
        print(f"{count} SECOND(S)!")
        count -= 1
    print("HAPPY NEW YEAR!") 
        
# countdown(count)


# countdown_with_sleep
def countdown_with_sleep(count):
    
    while count > 0:
        time.sleep(1)
        print(f"{count} SECOND(S)!")
        count -= 1
    print("HAPPY NEW YEAR!")
        
# countdown_with_sleep(count)