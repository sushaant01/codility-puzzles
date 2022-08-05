
public class MissingInteger{
    // you can also use imports, for example:
    // import java.util.*;
    
    // you can write to stdout for debugging purposes, e.g.
    // System.out.println("this is a debug message");
    
        public static void main(String[] args) {
            int A []= {1,2,3,4,5,6,7,8,9,10};
            System.out.println(getMissingInteger(A));
           
        }
        public static int getMissingInteger(int[] A) {

            int minElement =  1 ;
            int [] countArray = new int [100001];
            for (int i : A){
                if (i > 0 && i < 100001 ){
                    if (countArray[i-1] == 0 ){
                        countArray[i-1] = 1;
                    }
                }
            }
            for ( int i = 0 ; i < countArray.length ; i ++ ){
                if (countArray[i] == 0 ){
                    minElement = i + 1;
                    break;
                }

            }
            return minElement;

        }
    }
    
    