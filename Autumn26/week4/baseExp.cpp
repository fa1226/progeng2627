#include <iostream>
#include <cmath>

/*program reads x and n
sum betw i=1 and n, x^i
computes value for sum of powers 
(using std::pow to compute the powers) and prints the result.
*/

double sumofpowers(double base, double exp){
    double sum = 0;
    for(int i=1; i <= exp; i++){
        sum = sum + std::pow(base, i);
    }
    return sum;
}

int main(){
    double n, x;
    
    std::cout << "please enter a base x" << std::endl;
    std::cin >> x;
    
    std::cout << "please enter a sum exponent n" << std::endl;
    std::cin >> n;

    std::cout << "The result for sum of powers is " << sumofpowers(x, n) << std::endl;
    
}