template <typename T>
struct Node {
    T value;
    Node* left;
    Node* right;
};
 
// Cracking the Coding Interview, Question 4.7
// Design an algorithm and write code to find the first common ancestor of two
// nodes in a binary tree. Avoid storing additional nodes in a data structure.
Node* LCA (Node* root, Node* p, Node* q) {
    if (root == NULL) return NULL;
    if (root == p || root == q) return root;
    Node* L = LCA(root->left, p, q);
    Node* R = LCA(root->right, p, q);
    if (L && R) return root;
    if (L != NULL) return L;
    if (R != NULL) return R;
    return NULL;
}
