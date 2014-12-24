/*
 * =====================================================================================
 *
 *       Filename:  merge.cpp
 *
 *    Description:  given two arrays of strings, return a merged list
 *
 *        Version:  1.0
 *        Created:  12/23/2014 18:12:13
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <string>
#include <vector>

vector<string> merge (string[] a, string[] b) {
    vector<string> sentence;
    int len = sizeof(a)/sizeof(*a);
    for (int i = 0; i < len; ++i)
        sentence.push_back(a[i])
    len = sizeof(b)/sizeof(*b);
    for (int i = 0; i < len; ++i)
        sentence.push_back(b[i])
    return sentence;
}

string* merge2(string[] a, string[] b) {
    int aLen = sizeof(a);
    int bLen = sizeof(b);
    int sLen = aLen + bLen;
    string* s = new string[sLen];
    int i = 0;
    for (; i < aLen; ++i) s[i] = a[i];
    for (; i < sLen; ++i) s[i] = b[i];
    return s;
}
