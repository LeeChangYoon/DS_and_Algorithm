/*
원래는 하나하나 다 제곱하여 더한 다음에 N-1을 나눠주어 나머지를 구하는 방식으로 가려고 했다.
근데 RunTime Error가 나오네...?
*/

#include stdio.h
#include stdlib.h
#include string.h

int main() {
	int T;
	int N, j = 0;
	char num_temp = malloc(sizeof(char)  1000000000000);
	int ans = 0;

	scanf(%d, &T);

	while (T  0) {
		scanf(%d %s, &N, num_temp);

		for (int i = 0; i N; i++) {
			ans += num_temp[i] - '0';
		}

		j += 1;
		printf(#%d %d, j, ans % (N - 1));
		ans = 0;
		T--;
	}
}
