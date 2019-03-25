import random;
max_number = 1000000;
random.seed();
print "guesss a number between 1 and " + str(max_number); 

secret_number = random.randint(1,max_number);


   
guess=input("guess again ")

while guess != secret_number:

   if guess < secret_number:
      print "too low try again"

   if guess > secret_number:
      print "too high try again"
 
   guess=input("guess again ")
      

print "you got it B-)"
