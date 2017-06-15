// https://www.hackerrank.com/challenges/handshake
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        for(int a0 = 0; a0 < T; a0++){
            int N = in.nextInt();
            int handshakes = (N * (N - 1)) / 2;
            System.out.println(handshakes);
        }
    }
    
    /*
     * <0 -> 0
     * 0 -> 0
     * 1 -> 0
     * 2 -> 1
     * 3 -> 2 + 1
     * 4 -> 3 + 2 + 1
     * 5 -> 4 + 3 + 2 + 1
     * n -> n-1 + n-2 + n-3 + ... + 1
     * n -> (n - 1 + 1) * (n-1) / 2
     * n -> n * (n - 1) / 2
     */
}
