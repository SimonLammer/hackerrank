// https://www.hackerrank.com/challenges/find-point
import java.io.*;
import java.util.*;

public class Solution {
   
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine());
        for (int i = 0; i < n; i++) {
            String[] spl = in.readLine().split(" ");
            int p_x = Integer.parseInt(spl[0]);
            int p_y = Integer.parseInt(spl[1]);
            int q_x = Integer.parseInt(spl[2]);
            int q_y = Integer.parseInt(spl[3]);
            // r = q + pq
            int r_x = q_x + (q_x - p_x);
            int r_y = q_y + (q_y - p_y);
            System.out.println(String.format("%d %d", r_x, r_y));
        }
    }
}
