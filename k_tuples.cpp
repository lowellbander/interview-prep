#include <iostream>

using namespace std;

/* This untested an very likely not a solution to the problem.
 * (MongoDB)
 * */

/*print all k tuples in nums*/
void print_pairs(int[] nums, int k) {
    // create an array of iterators
    int[k] iterators;
   
    int place = 0;
    
    while (iterators[0] != len(nums) - k) { // maybe off by one
        // initialize all iterators
        for (int i = place; i < len(iterators); ++i) {
                iterators[i] = i;        
        }
        // start by moving the last iterator
        for (int i = len(iterators) - 1; iterators[i] < len(nums); ++i)
            for (int i = 0; i < len(iterators); ++i)
                cout << nums[iterators[i]] << ", ";
        ++place;
    
    }
}
