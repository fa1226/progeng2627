#include <iostream>

int main(){
    int n;
    std::cin >> n;

    // n times we draw one row
    // note that we need a different variable
    // for the loop counter
    int c2 = 1;
    while((c2-1) < n){

        // the following loop draws one row
        int c=1;
        while( (c-1) < n ){
            std::cout << (c*c2);
            std::cout << "\t";
            c++;
            // there is no << std::endl
            // because we want them on the same row    
        }

        std::cout << std::endl;
        c2++;
        // we go on a newline after each row

    }

}