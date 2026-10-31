/*Write a version of the sum of powers program that uses the function mypow
 you have implemented instead of std::pow.*/

#include <iostream>
#include <cmath>

double mypow(double base, int exp){
    double result=1;
    if (exp>0){
        for(int i=0; (i<exp); i++){
            result=result*base;
        }
    }
    else if ((exp<0)){
        double divisor=1;
        for(int i=exp; (i<0); i++){
            divisor=divisor*base;
        }
        result=result/divisor;
    }
    return result;
}

double sumofpowers(double base, double exp){
    double sum = 0;
    if (exp>0){
        for(int i=1; i < (exp+1); i++){
            sum = sum + mypow(base, i);
        }
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