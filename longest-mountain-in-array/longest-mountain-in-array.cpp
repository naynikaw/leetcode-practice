class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        int largest = 0;
        int cnt;
        for (int i=1; i<=n-2;){
            if (arr[i]>arr[i-1] and arr[i]>arr[i+1]){
                cnt = 1;
                int j = i;
                
                while(j>=1 and arr[j]>arr[j-1]){
                    j--;
                    cnt++;
                }
                
                while(i<=n-2 and arr[i]>arr[i+1]){
                    i++;
                    cnt++;
                }
            }
            
            else{
                i++;
            }
            largest = max(largest, cnt);
        }
        return largest;
    }
};