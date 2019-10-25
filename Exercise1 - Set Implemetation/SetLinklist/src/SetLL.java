public class SetLL {
    private int size;
    private LinkedList data;

    public SetLL(){
        data = new LinkedList();
        size = 0;
    }

    public boolean add(String word){
        if(data.contains(word)){
            return false;
        }
        else {
            data.insertfirst(word);
            size = size + 1;
            return true;
        }
    }
    public void travel(){
        data.printList();
    }

    public int size() {
        return size;
    }

    public boolean contains(String a){
        return data.contains(a);
    }
}
