public class SLList {
    private class ListNode {
        public String item;
        public ListNode next;

        public ListNode(String i, ListNode n) {
            item = i;
            next = n;
        }

        public ListNode() {
            item = (String) "";
            next = null;
        }
    }

    private ListNode first;
    private int size;

    public boolean contains(String a){
        ListNode temp = first;
        while(temp != null){
            if(temp.item.equals(a)){
                return true;
            }
            else{
                temp = temp.next;
            }
        }
        return false;
    }

    public SLList(String x) {
        first = new ListNode(x, null);
        size = 1;
    }

    public SLList() {
        first = new ListNode();
        size = 0;
    }

    /** Adds x to the front of the list. */
    public void addFirst(String x) {
        first = new ListNode(x, first);
        size += 1;
    }

    /** Returns the first item in the list. */
    public String getFirst() {
        return first.item;
    }

    /** Adds an item to the end of the list. */
    public void addLast(String x) {
        size += 1;

        ListNode p = first;

        /* Move p until it reaches the end of the list. */
        while (p.next != null) {
            p = p.next;
        }

        p.next = new ListNode(x, null);
    }

    public int size() {
        return size;
    }
    public ListNode insert(String data)
    {
        // Create a new node with given data
        ListNode new_node = new ListNode(data, null);
        ListNode head = first;
        // If the Linked List is empty,
        // then make the new node as head
        if (head == null) {
            head = new_node;
        }
        else {
            // Else traverse till the last node
            // and insert the new_node there
            ListNode last = head;
            while (last.next != null) {
                last = last.next;
            }

            // Insert the new_node at last node
            last.next = new_node;
        }

        // Return the list by head
        return first;
    }
}