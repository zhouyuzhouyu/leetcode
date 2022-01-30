import java.util.HashMap;
import java.util.HashSet;

public class P3 {

    public static void main(String[] args) {
        class Solution {
            public int lengthOfLongestSubstring(String s) {
                int result = 0;
                HashSet<Character> hashSet = new HashSet<Character>();
                int j = 1;

                for (int i = 0; i < s.length(); i++) {
                    hashSet.add(s.charAt(i));
                    if (i != 0) {
                        hashSet.remove(s.charAt(i - 1));
                    }
                    result = result > 0 ? result : 1;
                    while (j < s.length()) {
                        if (hashSet.contains(s.charAt(j))) {
                            break;
                        } else {
                            result = result < (j - i + 1) ? (j - i + 1) : result;
                            hashSet.add(s.charAt(j));
                        }
                        j++;
                    }

                }
                return result;
            }

        }
    }
}