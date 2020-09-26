class Solution {
public:
    bool isPalindrome(int x) 
    {
        if(x<0) return false;
        int temp=0;
        long rev=0;
        for(int y=x;y;)
        {
            temp=y%10;
            rev=rev*10+temp;
            y=y/10;
        }
        if(rev<=INT_MAX)
            return ((int)rev==x);
        else return false;
    }
};