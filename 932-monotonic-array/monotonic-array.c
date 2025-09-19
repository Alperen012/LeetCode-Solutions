bool isMonotonic(int* nums, int numsSize) {
    
    int is_increase = 2, is_increase_temp = 2, temp = nums[0];
    int i;
    for(i=1; i<numsSize; i++){
        if(temp<nums[i]){
            is_increase = 1;
        }
        else if(temp == nums[i]){
            is_increase = is_increase_temp;
        }
        else{
            is_increase = 0;
        }

        if(i==1){
            is_increase_temp = is_increase;
        }

        if(is_increase != is_increase_temp){
            if(is_increase_temp != 2){
                return false;
            }
            is_increase_temp = is_increase;
            
        }

        temp = nums[i];

    }

    return true;
}