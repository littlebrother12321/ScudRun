// choices
// by luke
#include <iostream>
int main(void)
{
   std::cout <<"answer 2 questions ready,go" <<std::endl;
   std::string name;
   std::cout << "please tell me your name" << std::endl;
   std::cin >> name;
   if(name == "Luke" || name == "luke")
   {
      std::cout << "Hello, " << name << " you are my favorite person" << std::endl;
   }
   else
   {
      std::cout << "Hello, " << name << " you allright I guess" << std::endl;
   }
   int mynumber;
   std::cout <<"tell me a number" <<std::endl;
   std::cin >> mynumber;
   std::cout << "watch me count to " << mynumber <<std::endl;
   for(int I=1;I<=mynumber;I++)
   {
      std::cout << I << std::endl;
   }
   return 0;
}
