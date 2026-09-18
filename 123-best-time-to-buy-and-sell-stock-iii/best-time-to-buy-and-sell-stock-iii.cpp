class Solution {
 public:
  int maxProfit(vector<int>& prices) {
    int sellTwo = 0;
    int holdTwo = INT_MIN;
    int sellOne = 0;
    int holdOne = INT_MIN;

    for (const int price : prices) {
     
   
   
