#include <iostream>
#include <vector>

int main(){
    std::vector<int> v;
    int n, num, t, i;

    std::cout << "Enter number n of numbers to read: " << std::endl;
    std::cin >> n;

    for (i=0; i<n; i++){
        std::cout << "Enter number to input: " << std::endl;
        std::cin >> num;
        v.push_back(num);

    }
    std::cout << "Enter number to compare with: " << std::endl;
    std::cin >> t;
    for (i=0; i<n; i++){
        if (v[i] < t){
            std::cout << v[i] << std::endl;
        }
    }
}