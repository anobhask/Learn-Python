import time
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
load_symbol = [ '.', '..', '...', '....', '.....', '......', '.......', '........']
i = 0
while True:
    i = (i + 1) % len(symbols)
    #print('\r\033[K%s loading%s' %(symbols[i],load_symbol[i]) flush=True, end='')
    print(f'\r {symbols[i]} loading{load_symbol[i]}', flush=True, end='')
    time.sleep(0.1)