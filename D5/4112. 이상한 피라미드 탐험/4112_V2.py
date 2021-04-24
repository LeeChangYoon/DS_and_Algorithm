'''
V1에서 비효율 적인 부분을 찾아 고쳐 푼 코드이다.
Layer(층) 단위로 점점 한 단계씩 내려가 연산 수를 줄일 수 있는 방법이 있었다. 
(예를 들면, 다음 수가 9라면 굳이 9를 찾을 필요 없이 6 ~ 10 사이에 있다는 것을 통해 연산을 통째로 넘어가고 다음 연산으로 가는 것이다.)
이런식으로 내려가면서 참색을 진행해 주면 V1코드보다 연산 수가 줄어 더 효율적이게 된다.
'''

def find_cnt(A):
  cnt = 0
  l, r = 0, 0
  while A <= B:
      if A == B:
          if l + r == 0:
              return b - a
          if l > b:
              cnt += l - b
          if r < b:
              cnt += b - r
          return cnt

      cnt += 1
      nl, nr = 0, 0
      if l + r == 0:
          if a + A == b or a + A + 1 == b:
              return cnt
          nl = a + A
          nr = a + A + 1

      else:
          if l + A <= b and b <= r + A + 1:
              return cnt
          nl = l + A
          nr = r + A + 1

      l = nl
      r = nr
      A += 1



data = []
i = 0
num = 0
while True:
  num += i
  data.append(num)
  i += 1
  if num > 10000:
      break


for tc in range(int(input())):
  a, b = map(int, input().split())
  A, B = 0, 0
  result = 0
  for i in range(len(data) + 1):
      if a <= data[i] and b <= data[i]:
          A += 1
          B += 1
          break
      if a > data[i]:
          A = i
      if b > data[i]:
          B = i

  if a == b:
      print(f"#{tc + 1} {result}")
      continue

  # 무조건 a가 작게 == 아래로 내려가게
  if a > b:
      a, b = b, a
      A, B = B, A

  result = find_cnt(A)


  print(f"#{tc + 1} {result}")
