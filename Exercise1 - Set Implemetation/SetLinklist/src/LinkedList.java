public class LinkedList {
    private class ListNode {
        String val;
        ListNode next;
        ListNode(String x) {
            val = x;
            next = null;
        }
    }

    ListNode head;

    public LinkedList() {
        head = null;
    }

//    public void add(String in) {
//        ListNode data = new ListNode(in);
//        data.next = head;
//        head = data;
//    }

    public void insert(String in) {
        ListNode data = new ListNode(in);
        ListNode current = head;
        if (head == null) {
            head = data;
            return;
        }
        while (current.next != null) {
            current = current.next;
        }
        current.next = data;
    }
    public void insertfirst(String str){
        ListNode data = new ListNode(str);
        if (head == null) {
            head = data;
            return;
        }
        else{
            data.next = head;
            head = data;
            return;
        }

    }

    public boolean contains(String a) {
        ListNode temp = head;
        while (temp != null) {
            if (temp.val.equals(a)) {
                return true;
            } else {
                temp = temp.next;
            }
        }
        return false;
    }

    public void printList() {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.println();
    }
}

