public class P5 {
    public static void main(String[] args) {
        new Solution().longestPalindrome("bb");
    }
    public static
    class Solution {

        public String longestPalindrome(String s) {
            if (s == null || s.length() <= 1) {
                return s;
            }

            int begin = 0;
            int last = 0;
            for (int i = 0; i < s.length()-1; i++) {
                int len1 = lenPalindome(s,i,i);
                int len2 = lenPalindome(s,i,i+1);
                int maxLen = Math.max(len1, len2);

                if (maxLen > last - begin + 1) {
                    begin = i - (maxLen-1)/2;
                    last = i + maxLen/2;
                }

            }
            return s.substring(begin,last+1);
            
        }
        private int lenPalindome(String s, int beginIndex, int lastIndex) {
            while (beginIndex < s.length() && beginIndex >= 0 && lastIndex < s.length() && s.charAt(beginIndex) == s.charAt(lastIndex)) {
                beginIndex--;
                lastIndex++;
            }
            return lastIndex- beginIndex - 1;
        }

    }


}