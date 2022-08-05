class MaxCounters{
// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

    public static void main(String[] args) {
        int N = 5;
        int A []= {3,4,4,6,1,4,4};
        for (int i : getMaxCounters(N,A)){
            System.out.println(i);
        }
        
    }
    public static int[] getMaxCounters(int N, int[] A) {
        // write your code in Java SE 8
        int[] arrayMaxCounter = new int[N];
        int maxCounter = 0;
        int lastMaxCounter = 0;
        for (int i = 0; i < A.length ; i ++){
            if (A[i]> N){
                lastMaxCounter = maxCounter;
            }else {
                if (arrayMaxCounter[A[i]-1] <  lastMaxCounter){
                    arrayMaxCounter[A[i]-1] = lastMaxCounter + 1 ;
                }else {
                    arrayMaxCounter[A[i]-1] += 1;
                }
                if (arrayMaxCounter[A[i]-1] > maxCounter ){
                    maxCounter = arrayMaxCounter[A[i]-1];
                }
            }
        }
        if (A[A.length-1] > N ){
            for(int i = 0; i < arrayMaxCounter.length ; i ++){
                arrayMaxCounter[i] = maxCounter ;   
            }
        }else{
            for(int i = 0 ; i < arrayMaxCounter.length ; i ++){
                if (arrayMaxCounter[i] < lastMaxCounter )   {
                    arrayMaxCounter[i] = lastMaxCounter;
                }
            }
        }
        return arrayMaxCounter;
    }
}


class Solution {


}