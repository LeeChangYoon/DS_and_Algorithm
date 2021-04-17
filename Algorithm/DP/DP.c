#include<stdio.h>

int N;
int dp[2][100001];
int board[2][100001];

const int max(const int a, const int b)
{
	return (a<b) ? b : a;
}

void findSticker()
{
	dp[0][0] = board[0][0];
	dp[1][0] = board[1][0];
	dp[0][1] = dp[1][0] + board[0][1];
	dp[1][1] = dp[0][0] + board[1][1];
	int i;
	for (i = 2; i < N; i++)
	{
		printf("highlighted %d %d\n", 2, i);
		printf("highlighted %d %d\n", 2, i - 2);
		printf("highlighted %d %d\n", 3, i - 2);
		printf("highlighted %d %d\n", 3, i - 1);
		dp[0][i] = max(dp[0][i - 2], dp[1][i - 2]);
		dp[0][i] = max(dp[1][i - 1], dp[0][i]);
		dp[0][i] += board[0][i];
		printf("updated %d %d\n", 0, i);
		printf("unhighlight\n");
		printf("unhighlight\n");

		printf("highlighted %d %d\n", 3, i);
		printf("highlighted %d %d\n", 2, i - 2);
		printf("highlighted %d %d\n", 3, i - 2);
		printf("highlighted %d %d\n", 2, i - 1);
		dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]);
		dp[1][i] = max(dp[0][i - 1], dp[1][i]);
		dp[1][i] += board[1][i];
		printf("updated %d %d\n", 1, i);
		printf("unhighlight\n");
		printf("unhighlight\n");
	}
}

int main()
{
	int T;
	int i, j;
	scanf("%d", &T);

	for (int test_case = 1; test_case <= T; test_case++)
	{
		printf("#%d ", test_case);
		scanf("%d", &N);
		for (j = 0; j < 2; j++)
		{
			for (i = 0; i < N; i++)
			{
				printf("highlighted %d %d\n", j, i);
				scanf("%d", &board[j][i]);
			}
		}
		findSticker();
		printf("%d\n", max(dp[0][N - 1], dp[1][N - 1]));
	}

	return 0;
}