line = input('>>> ')

flag="pctf{Un1c0d3_i5_sw34t}"

if len(line) > 9:
    raise Exception()

try:
    eval(line)
except:
    pass
