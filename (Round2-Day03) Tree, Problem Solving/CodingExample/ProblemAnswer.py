def solution(N, A, B):
      answer = 0

      while A != B:
           A = (A + 1) // 2
           B = (B + 1) // 2
           answer += 1
      
      return answer