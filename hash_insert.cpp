/*
 * =====================================================================================
 *
 *       Filename:  hash_insert.cpp
 *
 *    Description:  Given a list of Student objects, return a mapping of {sid:
 *    Student}
 *
 *        Version:  1.0
 *        Created:  12/23/2014 17:50:33
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Lowell Bander
 *   Organization:  
 *
 * =====================================================================================
 */
#include <map>

using namespace std;

unordered_map<int, Student> buildMap (Student[] students) {
    int len = sizeof(students)/sizeof(Student);
    unordered_map<int, Student> mapping;
    for (int i = 0; i < len; ++i)
        mapping.emplace(students[i].getID(), students[i])
    return mapping;
}
