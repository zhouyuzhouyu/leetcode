public class P2 {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }

    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode l1New = l1;
            ListNode l2New = l2;

            ListNode result = null;
            ListNode current = null;

            int s = 0;

            while(l1New!=null || l2New!=null || s!=0) {
                int v1 = 0;
                int v2 = 0;
                if(l1New!=null) {
                    v1 = l1New.val;
                    l1New = l1New.next;
                }
                if (l2New != null) {
                    v2 = l2New.val;
                    l2New = l2New.next;
                }

                int r =  v1 + v2 + s;
                if (r >= 10) {
                    r -= 10;
                    s = 1;
                } else {
                    s = 0;
                }

                if (result == null) {
                    result = new ListNode(r);
                    current = result;
                } else {
                    current.next = new ListNode(r);
                    current = current.next;
                }




            }

            return result;

        }
    }

}




