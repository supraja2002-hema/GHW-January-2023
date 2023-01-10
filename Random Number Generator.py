import time
def randn(minimum,maximum):
    now=str(time.perf_counter())
    rnd=float(now[::-1][:3:])/1000
    print(round(minimum + rnd*(maximum-minimum)))

mini=int(input("Minimum number:"))
maxi=int(input("Maximum number:"))
randn(mini,maxi)
