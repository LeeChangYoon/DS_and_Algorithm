/*
그래서 구글링을 해보니, '페르마의 소정리' 라는 걸 이용하는 방법이 나왔다.
이 정리에 대해 궁금하면 구글링 해보고, 아주 신박한 방법이였다.
*/

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
