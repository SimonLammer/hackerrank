// https://www.hackerrank.com/challenges/bon-appetit
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static long bonAppetit(int n, int k, int b, int[] ar) {
        long sum_without_k = 0;
        for (int i = 0; i < ar.length; i++) {
            if (i != k) {
                sum_without_k += ar[i];
            }
        }
        return b - (sum_without_k / 2);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] ar = new int[n];
        for(int ar_i = 0; ar_i < n; ar_i++){
            ar[ar_i] = in.nextInt();
        }
        int b = in.nextInt();
        long result = bonAppetit(n, k, b, ar);
        System.out.println(result == 0 ? "Bon Appetit" : result);
    }
}
