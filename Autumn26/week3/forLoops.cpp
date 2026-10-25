#include <iostream>

int main(){
    int n, x, num;

    std::cout << "Please enter a number n" << std::endl;
    std::cin >> n;

    std::cout << "Please enter a number x" << std::endl;
    std::cin >> x;

    num = x;

    for(int i = 0; i < (n - 1); i++){
        num = num * x;
    }

    std::cout << num << std::endl;
}

/*
Write a program that computes x^n (whith n integer >= 0) as repeated multiplications by 
using a for loop.
*/