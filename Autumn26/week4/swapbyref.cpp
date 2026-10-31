// wrong version!
#include <iostream>
/*Write a functions which swaps variables containing text (i.e. of type std::string). 
Write a main to test the function.*/

void myswap(std::string& a, std::string& b){

    std::string tmp;
    tmp = a;
    a = b;
    b = tmp;

}

int main(){
    std::string str1, str2;

    std::cout << "please enter two texts" << std::endl;
    std::cin >> str1 >> str2;

    std::cout << "you entered:" << std::endl;
    std::cout << "Text 1: " << str1 << std::endl;
    std::cout << "Text 2: " << str2 << std::endl;

    myswap(str1, str2);
    // here a becomes another name for n1
    // while b becomes another name for n2

    // it's just about the position/order in the parentheses:
    // n1 is passed to the first parameter (a)
    // n2 is passed to the second parameter (b)

    std::cout << "after swapping the texts:" << std::endl;
    std::cout << "Text 1: " << str1 << std::endl;
    std::cout << "Text 2: " << str2 << std::endl;
}
