
#include <iostream>
#include <set>
#include <unordered_set>
#include <ctime>

using namespace std;



int main()
{
    multiset <int> multiSet;
    unordered_multiset <int> unorderedMultiSet;

    int n = 2500000;

    clock_t multiSetStart = clock();

    for(int i = 0; i < n; ++i)
    {
        int randNum = rand();
        multiSet.insert(randNum);
    }

    clock_t multiSetTime = clock() - multiSetStart;

    clock_t unorderedMultiSetStart = clock();

    for(int i = 0; i < n; ++i)
    {
        int randNum = rand();
        unorderedMultiSet.insert(randNum);
    }

    clock_t unorderedMultiSetTime = clock() - unorderedMultiSetStart;

    cout << "N: " << n << endl;
    cout << "Multiset Time: " << ((double) multiSetTime) / (double) CLOCKS_PER_SEC << endl;
    cout << "Unordered Multiset Time: " << ((double) unorderedMultiSetTime) / (double) CLOCKS_PER_SEC << endl;

    return 0;
}



