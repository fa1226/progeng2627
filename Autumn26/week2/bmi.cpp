/*
BMI calculator¶
According to https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/calculate-bmi-for-adults:

The BMI is calculated by dividing an adult's weight in kilograms by their height in metres squared.

For example, if you weigh 70kg (around 11 stone) and are 1.70m (around 5 foot 7 inches) tall, you work out your BMI by:

squaring your height in metres: 1.70 x 1.70 = 2.89 dividing your weight in kilograms: 70 ÷ 2.89 = 24.22 Your result will be displayed to one decimal place, for example, 24.2.

Write a program that: - Prints a prompt for the user to enter the relevant information - Reads and stores in suitable variables the information - Computes the resulting BMI - Prints the BMI

To compute the square you can just multiply the relevant variable times itself (the operator ^ exists in C++ but it is for something else).
*/


#include <iostream>

int main(){
    double bmi, weight, height;
    std::cout << "what is your weight in kilograms?" << std::endl;
    std::cin >> weight;

    std::cout << "what is your height in metres?" << std::endl;
    std::cin >> height;

    bmi = weight / (height*height);

    std::cout << "your bmi is " << bmi << std::endl;

}