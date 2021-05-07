import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        String[] s = null;
        int N = 0;
        String str = "";
        int sum = 0;

        for(int t=1;t<=T; t++) {
            s = br.readLine().split(" ");
            N = Integer.parseInt(s[0]);
            str = s[1];
            sum = 0;
            for(int i=0; i<str.length(); i++) {
                sum += Integer.parseInt(str.substring(i, i+1));
            }
            bw.write("#"+t+" "+(sum%(N-1))+"\n");
        }

        br.close();
        bw.close();
    }
}