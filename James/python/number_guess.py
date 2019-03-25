import random;
max_number = 100;
random.seed();
print "guesss a number between 1 and " + str(max_number); 

secret_number = random.randint(1,max_number);



guess = 0;
 
while guess != secret_number:
   guess=input("guess again");
   print "you guessed " + str(guess);

print "you got it"
