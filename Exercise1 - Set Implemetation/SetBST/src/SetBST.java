public class SetBST {
    private int size;
    private BinarySearchTree data;

    public SetBST(){
        data = new BinarySearchTree();
        size = 0;
    }

    public boolean add(String word){
        if(data.contains(word)){
            return false;
        }
        else {
            data.insert(word);
            size = size + 1;
            return true;
        }
    }

    public int size() {
        return size;
    }

    public boolean contains(String a){
        return data.contains(a);
    }
}


