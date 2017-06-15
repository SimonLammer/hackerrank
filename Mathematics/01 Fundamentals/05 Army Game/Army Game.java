// https://www.hackerrank.com/challenges/game-with-cells
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        System.out.println((int)Math.ceil(m / 2.0) * (int)Math.ceil(n / 2.0));
    }
}
