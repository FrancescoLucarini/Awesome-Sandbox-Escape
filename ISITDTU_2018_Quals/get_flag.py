secret = "392a3d3c2b3a22125d58595733031c0c070a043a071a37081d300b1d1f0b09".decode("hex")
key = "pythonwillhelpyouopenthedoor"
result = ""
for i in xrange(len(secret)):
        result += chr(ord(secret[i]) ^ ord(key[i % len(key)]))
print result
