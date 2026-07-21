class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevMap = new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int comp = target - nums[i];

            if (prevMap.containsKey(comp)){
                return new int[] {prevMap.get(comp), i};
            } 
            prevMap.put(nums[i],i);

        }
        return new int[] {};
    }
}