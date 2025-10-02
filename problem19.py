# 19.Fibonacci sequence – generate series or nth term.

seq = [0,1]
def get_values():
    n = int(input("How many terms do you want:"))
    for _ in range(n):
       total= seq[-1]+seq[-2]
       seq.append(total)
get_values()
print(seq)

