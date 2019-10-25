public class BinarySearchTree {
    /* Class containing left and right child of current node and key value*/
    private class Node {
        private String key;
        private Node left, right;

        private Node(String item) {
            key = item;
            left = right = null;
        }
    }

    // Root of BST
    private Node root;

    // Constructor
    public BinarySearchTree() {
        root = null;
    }

    // This method mainly calls insertRec()
    public void insert(String key) {
        root = insertRec(root, key);
    }

    /* A recursive function to insert a new key in BST */
    private Node insertRec(Node root, String key) {
        /* If the tree is empty, return a new node */
        if (root == null) {
            root = new Node(key);
            return root;
        }

        /* Otherwise, recur down the tree */
        if (key.compareTo(root.key)<0)
            root.left = insertRec(root.left, key);
        else if (key.compareTo(root.key)>0)
            root.right = insertRec(root.right, key);

        /* return the (unchanged) node pointer */
        return root;
    }

    // This method mainly calls InorderRec()
    public void inorder()  {
        inorderRec(root);
    }

    // A utility function to do inorder traversal of BST
    private void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.println(root.key);
            inorderRec(root.right);
        }
    }

    public boolean contains(String k){
        return check(root, k);
    }

    private boolean check(Node start, String key){
        Node temp = start;
        if (temp == null) {
            return false;
        }

        if (key.compareTo(temp.key)<0)
            return check(temp.left, key);
        else if (key.compareTo(temp.key)>0)
            return check(temp.right, key);
        else{
            return true;
        }
    }
}
