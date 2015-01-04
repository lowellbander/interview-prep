#include <climits>

struct Node {
    T value;
    Node* left;
    Node* right;
};

// Cracking the Coding Interview, Question 4.5
// Implement a function to check if a binary tree is a binary search tree
bool isSearch(Node* root, int max = INT_MAX, int min = INT_MIN) {
  if (!root) return true;
  if (root->value <= min || root->value > max)
    return false;
  return isSearch(root->left, root->value, min) && isSearch(root->right, max, root->value);
}
