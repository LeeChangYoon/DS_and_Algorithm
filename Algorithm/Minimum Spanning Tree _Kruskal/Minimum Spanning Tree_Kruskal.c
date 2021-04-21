#include <stdio.h>

const int MAXV = 100005;
const int MAXE = 500005;

struct EDGE {
	int x, y, w;
} edge[MAXE], tmp[MAXE];

int V, E;
int disjoint_set[MAXV];

int find_root(int x) {

	if (disjoint_set[x] == x)
		return x;

	disjoint_set[x] = find_root(disjoint_set[x]);

	return disjoint_set[x];
}

void MergeSort(int s, int e) {
	if (s < e) {
		int m = (s + e) / 2;
		MergeSort(s, m);
		MergeSort(m + 1, e);
		int left = s, right = m + 1, pointer = s;
		while (left <= m && right <= e) {
			if (edge[left].w <= edge[right].w) {
				tmp[pointer++] = edge[left++];
			}
			else {
				tmp[pointer++] = edge[right++];
			}
		}
		while (left <= m) tmp[pointer++] = edge[left++];
		while (right <= e) tmp[pointer++] = edge[right++];
		for (int i = s; i <= e; i++) {
			edge[i] = tmp[i];
		}
	}
}

void Kruskal(void) {
	int mst_total_weight = 0;

	for (int i = 0; i < E; i++) {

		int group_x = find_root(edge[i].x);
		int group_y = find_root(edge[i].y);

		if (group_x == group_y) {
			continue;
		}

		mst_total_weight += edge[i].w;

		disjoint_set[group_y] = group_x;
		printf("Union %d - %d\n", group_x, group_y);
	}

	printf("%d\n", mst_total_weight);
}

int main(void) {

	int TC; for (scanf("%d", &TC); TC--;) {

		scanf("%d%d", &V, &E);

		for (int i = 1; i <= V; i++) {
			printf("Draw vertex %d\n", i);
			disjoint_set[i] = i;
		}

		for (int i = 0; i < E; i++) {
			scanf("%d%d%d", &edge[i].x, &edge[i].y, &edge[i].w);
		}

		MergeSort(0, E - 1);

		static int testcase = 0;
		printf("#%d ", ++testcase);

		Kruskal();
	}
	return 0;
}