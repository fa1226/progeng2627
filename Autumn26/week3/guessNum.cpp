/*Write a program which "guesses" (better: finds out using an algorithm) what (integer) number
 the user is thinking, given a range (lower bound and higher bound) and, after each attempt, 
 feedback from the user on whether the attempted value is less or greater than the actual number.*/
#include <iostream>

int main(){
    int UB, LB, mid;
    bool correct_answer = false;
    
    std::cout << "Enter an upper bound" << std::endl;
    std::cin >> UB;

    std::cout << "Enter a lower bound" << std::endl;
    std::cin >> LB;

    while (correct_answer == false){

        mid = ((UB + LB) /2);
        
        std::string guess;
        std::cout << "Correct, or higher or lower than " << mid << "?" << std::endl;
        std::cin >> guess;

        if (guess == "higher"){
            LB = mid;
        }
        else if (guess == "lower"){
            UB = mid;
        }
        else if (guess == "correct"){
            correct_answer = true;
        }
    }
    std::cout << mid << " is correct.";
}