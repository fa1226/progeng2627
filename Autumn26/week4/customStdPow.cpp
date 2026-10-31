#include <iostream>

/*Extend the program above so that mypow can deal also with negative (integer) exponents. 
Edit the main so that it includes an example also testing this case.*/

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

int main(){
    // we test examples with integer (and non-negative) exponent

    std::cout << "2^3: " << mypow(2, 3) << std::endl;
    std::cout << "0.5^2: " << mypow(0.5, 2) << std::endl;
    std::cout << "1^0: " << mypow(1, 0) << std::endl;
    std::cout << "2^-3: " << mypow(2, -3) << std::endl;
}