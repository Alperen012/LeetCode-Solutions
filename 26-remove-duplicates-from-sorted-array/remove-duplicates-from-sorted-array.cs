public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int i=0;
        int temp=-111;
        foreach(int num in nums){
            if(temp!=num){
                nums[i] = num;
                i++;
            }
            temp=num;
        }
        return i;
    }
}