import java.util.Arrays;

public class P4 {
/*        public double findMedianSortedArrays(int[] nums1, int[] nums2) {
            int[] nums = new int[nums1.length + nums2.length];
            for (int i = 0; i < nums.length; i++) {
                if (i < nums1.length) {
                    nums[i] = nums1[i];
                } else {
                    nums[i] = nums2[i - nums1.length];
                }
            }

            Arrays.sort(nums);
            if (nums.length <= 0) {
                return 0;
            }

            double result = 0;
            if (nums.length % 2 == 0 ) {
                result = (nums[nums.length/2] + nums[nums.length/2 - 1])/2.0d;
            } else {
                result = nums[nums.length/2];
            }
            return result;

        }
    }*/



/*
        public static void main(String[] args) {
            class Solution {
                public double findMedianSortedArrays(int[] nums1, int[] nums2) {

                    int n1 = nums1.length;
                    int n2 = nums2.length;

                    if (n1 + n2 <= 0) {
                        return 0;
                    }

                    int resultIndex1 = 0;
                    int resultIndex2 = 0;

                    if ((n1 + n2) % 2 == 0) {
                        resultIndex1 = (n1 + n2) / 2 - 1;
                        resultIndex2 = (n1 + n2) / 2;
                    } else {
                        resultIndex1 = (n1 + n2) / 2;
                        resultIndex2 = resultIndex1;
                    }

                    int index1 = 0;
                    int index2 = 0;

                    int result1 = 0;
                    int result2 = 0;


                    int currentIndex = 0;
                    while (index1 < nums1.length || index2 < nums2.length) {
                        int resultT = 0;
                        if (index1 >= nums1.length) {
                            resultT = nums2[index2];
                            index2++;
                        } else if (index2 >= nums2.length) {
                            resultT = nums1[index1];
                            index1++;
                        } else {
                            if (nums1[index1] <= nums2[index2]) {
                                resultT = nums1[index1];
                                index1++;

                            } else {
                                resultT = nums2[index2];
                                index2++;

                            }
                        }



                        if (resultIndex1 == currentIndex) {
                            result1 = resultT;
                        }
                        if (resultIndex2 == currentIndex) {
                            result2 = resultT;
                            break;
                        }
                        currentIndex++;


                    }
                    return (result1 + result2) * 0.5;
                }

            }

            int[] sum1 = new int[2];
            sum1[0] = 1;
            sum1[1] = 3;
            int[] sum2 = new int[1];
            sum2[0] = 2;
            new Solution().findMedianSortedArrays(sum1,sum2);

        }

 */
    public static void main(String[] args) {
        int[] sum1 = new int[2];
        sum1[0] = 1;
        sum1[1] = 2;
        int[] sum2 = new int[2];
        sum2[0] = 3;
        sum2[1] = 4;
        double s =  new Solution().findMedianSortedArrays(sum1,sum2);
        System.out.println(s);
    }
static class Solution {


    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;

        if (n1 + n2 == 0) {
            return 0;
        }

        if ((n1 + n2) % 2 == 0) {
            return (findK(nums1, 0, n1-1, nums2, 0, n2-1, (n1+n2)/2) +
                    findK(nums1, 0, n1-1, nums2, 0, n2-1, (n1+n2)/2+1)) * 0.5;
        } else {
            return findK(nums1, 0, n1-1, nums2, 0, n2-1, (n1+n2)/2+1);
        }
    }
    private double findK(int[] nums1, int prevIndex1, int lastIndex1, int[] nums2, int prevIndex2, int lastIndex2, int k) {
        int n1 = lastIndex1 - prevIndex1 + 1;
        int n2 = lastIndex2 - prevIndex2 + 1;

        if (n1 > n2) {
            return findK(nums2, prevIndex2, lastIndex2, nums1, prevIndex1, lastIndex1, k);
        }

        if (n1 <= 0) {
            return nums2[prevIndex2 + k - 1];
        }

        if (k == 1) {
            return Math.min(nums1[prevIndex1], nums2[prevIndex2]);
        }

        int removeK = Math.min(k/2,n1);

        if (nums1[prevIndex1 + removeK - 1] <= nums2[prevIndex2 + removeK - 1]) {
            return findK(nums1, prevIndex1 + removeK, lastIndex1, nums2, prevIndex2, lastIndex2, (k - removeK));
        } else {
            return findK(nums1, prevIndex1 , lastIndex1, nums2, prevIndex2 + removeK, lastIndex2, (k - removeK));
        }

    }
}

}