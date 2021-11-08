#include <iostream>
using namespace std;

int main()
{
    int age = 24;
    double gpa = 4.3;

    /*
    must use single quatations ('') for single character 
    must use double quatations ("") for multiple characters
    */
    char letter = 'j';
    string characterName = "Hafiz";

    // t from true is NOT capitalized
    bool isMale = true;
    cout << "Enter your Name: "; 

    // replace current value for user's 
    getline(cin, characterName);

    cout << "Enter your age: ";
    cin >> age;

    int luckyNums[3] = {4, 13};
    luckyNums[2] = age;
    
    /*
    prints output with separators (<<) separating data types
    most useful feature of C++ other than the fact that it is faster
    */

    cout << "Hello " << characterName << "!\nYour age is " << luckyNums[2] << endl;
    return 0;   
}       


