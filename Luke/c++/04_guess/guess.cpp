// Guess
// by luke, with help from Dad
#include <iostream>
#include <stdlib.h>

#define HIGHEST_NUMBER 100

int main(void)
{
  srand(time(NULL));
  int myNumber = rand() % HIGHEST_NUMBER +1;
  int guessedNumber = -1;
  std::cout <<"I'm Thinking of a number between 1 and "
	    << HIGHEST_NUMBER << " Can you guess it?" <<std::endl;
  while(guessedNumber != myNumber)
    {
     //guessedNumber = guessedNumber +1;
     //std::cout <<"how about " <<guessedNumber<< std::endl; 
     std::cin >>guessedNumber;
     if(guessedNumber<myNumber)
     {
      std::cout <<"too low try again" << std::endl;
     }
     if (guessedNumber > HIGHEST_NUMBER +1)
     {
      std::cout <<"out of range reset the game" <<std::endl;
     }
     else if(guessedNumber>myNumber)
     {
      std::cout <<"too high try again" << std::endl;

  std::cout << "You got it!, my number was " << myNumber << std::endl;
}
   return 0;}}

