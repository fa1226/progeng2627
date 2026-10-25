#include <iostream>

/*Take any n. n even, get n/2. n odd, obtain 3n + 1. Repeat indefinitely. 
you shall always eventually reach 1.
a program which reads a (natural) number from the user and prints the corresponding sequence*/

int main(){
    int n, curmax, counter=0;

    std::cout << "please enter number:" << std::endl;
    std::cin >> n;
    curmax = n;


    std::cout << n;
    std::cout << "\t";

    while(n!= 1){

        if (n%2 ==0){
            n = n/2;
            std::cout << n;
            std::cout << "\t";
        }
        else{
            n = (n*3 + 1);
            std::cout << n;
            std::cout << "\t";
        }
        if (n > curmax){
            curmax = n;
        }
        counter++;
    }
    std::cout << std::endl;
    std::cout << "The maximum number generated was " << curmax << std::endl; 
    std::cout << "The sequence took " << counter << " steps.";
}