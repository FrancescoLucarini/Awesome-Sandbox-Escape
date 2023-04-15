line = input('>>> ')

flag="pctf{JusT_a5k_4_h3lP!}"

if len(line) > 10:
    raise Exception()

try:
    eval(line)
except:
    pass
