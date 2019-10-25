public class SetLL {
    private int size;
    private SLList data;

    public SetLL(String a){
        data = new SLList(a);
        size = 1;
    }

    public SetLL(){
        data = new SLList();
        size = 0;
    }

    public boolean add(String word){
        if(data.contains(word)){
            return false;
        }
        else {
            data.addLast(word);
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
