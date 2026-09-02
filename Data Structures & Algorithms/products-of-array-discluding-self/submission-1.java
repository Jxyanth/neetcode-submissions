class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        for(int i=0;i<nums.length;i++){
            res[i] = 1;
        }
        int prefix = 1;
        for(int i=0;i<res.length;i++){
            res[i]=res[i]*prefix;
            prefix = prefix*nums[i];
        }
        int postfix = 1;
        for(int i=res.length-1;i>-1;i--){
            res[i] = res[i]*postfix;
            postfix = postfix*nums[i];
        }
        return res;
    }
}  
