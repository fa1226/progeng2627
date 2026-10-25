#include <iostream>

int main(){
    int n, num;

    std::cout << "Please enter a number n" << std::endl;
    std::cin >> n;

    num = n;

    if (num == 0){
        num = 1;
    }

    for(int i = (n-1); i >= 1; i--){
        num = num * i;
    }

    std::cout << num << std::endl;
}