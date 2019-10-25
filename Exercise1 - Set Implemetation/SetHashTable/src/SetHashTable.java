import java.util.Arrays;

public class SetHashTable{
    private static final double MAX_LOAD = 0.75;   // load factor on which to rehash
    private Node[] buckets;
    private int size;

    // Constructs a new empty set of integers.
    public SetHashTable() {
        buckets = (Node[]) new SetHashTable.Node[10];
        size = 0;
    }

    public int getHashCode(String word) {
        int h = 0;
        if (h == 0 && word.length() > 0) {
            char[] val = word.toCharArray();

            for (int i = 0; i < val.length; i++) {
                h = 31 * h + val[i];
            }
        }
        return h;
    }

    // Adds the given value to this set,
    // if it was not already contained in the set.
    public boolean add(String value) {
        // linear probing to find proper index
        if (!contains(value)) {
            int h = hash(value);
            Node newNode = new Node(value);
            newNode.next = buckets[h];
            buckets[h] = newNode;
            size++;
            if (loadFactor() > MAX_LOAD) {
                rehash();
            }
            return true;

        }

        // resize if necessary
        return false;
    }

    // Returns whether the given value is found in this set.
    public boolean contains(String value) {
        // linear probing to find proper index
        int h = hash(value);
        Node current = buckets[h];
        while (current != null) {
            if (current.data.equals(value)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    // Returns true if there are no buckets in this set.
    public boolean isEmpty() {
        return size == 0;
    }

    // Returns the hash table's "load factor", its ratio of size to capacity.
    public double loadFactor() {
        return (double) size / buckets.length;
    }

    // Removes the given element value from this set,
    // if it was found in the set.
    public void remove(String value) {
        // linear probing to find proper index
        int h = hash(value);

        if (buckets[h] != null) {
            // front case
            if (buckets[h].data.equals(value)) {
                buckets[h] = buckets[h].next;
            } else {
                // non-front case
                Node current = buckets[h];
                while (current.next != null &&
                        !current.next.data.equals(value)) {
                    current = current.next;
                }

                // current.next == null
                // || current.next.data == value
                if (current.next != null) {
                    current.next = current.next.next;
                }
            }
        }
    }

    // Returns the number of buckets in this set.
    public int size() {
        return size;
    }

    // Returns a text representation of this set.
    public String toString() {
        return Arrays.toString(buckets);
    }

    // hash function for mapping values to indexes
    private int hash(String value) {
        return Math.abs(getHashCode(value)) % buckets.length;
    }

    // Resizes the hash table to twice its original capacity.
    private void rehash() {
        Node[] newbuckets = (Node[]) new SetHashTable.Node[2 * buckets.length];
        Node[] old = buckets;
        buckets = newbuckets;
        size = 0;
        for (Node node : old) {
            while (node != null) {
                add(node.data);
                node = node.next;
            }
        }
    }

    private class Node {
        public String data;
        public Node next;

        public Node(String data) {
            this.data = data;   //成员变量和形参名字一样，所以需要使用this
        }
    }
}
