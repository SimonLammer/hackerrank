// https://www.hackerrank.com/challenges/lowest-triangle
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int lowestTriangle(int base, int area){
        return (int) Math.ceil(2.0 * area / base);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int base = in.nextInt();
        int area = in.nextInt();
        int height = lowestTriangle(base, area);
        System.out.println(height);
    }
    
    /*
     * a <= b * h / 2
     * 2a / b <= h
     */
}
