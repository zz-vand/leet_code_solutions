haystack = "sddsadbutsad"
needle = "sad"


if haystack.count(needle) == 0:
    print(-1)

hs = haystack.split(needle)
print(len(hs[0]))