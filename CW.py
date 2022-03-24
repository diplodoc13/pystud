n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
nm = n + m - x - t
km = m + k - y - t
nk = n + k - z - t
one = (n - nm - t - nk) + (m - nm - t - km) + (k - km - t - nk)
two = nm + km + nk
no_one = a - one - two - t
print(one)
print(two)
print(no_one)
