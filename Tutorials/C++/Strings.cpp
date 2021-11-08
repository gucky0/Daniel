#include <iostream>
using namespace std;

int main()
{
    string phrase = "Dad is sad";

    // same indexing as python
    phrase[7] = 'm';
        
    cout << phrase << endl;

    // this is used to find a letter or phrase
    // cout << phrase.find('d');
    // cout << phrase.find('d',3);


    // this is used to extract data based on index only
    // cout << phrase.substr(4,2);

    return 0;   
}       


