from math import ceil

def f(x):
    if x >= 10000000:
        return x - 3
    else:
        fs_ate_10_milhoes = ceil((10000000 - x) / 13)

        x += 13 * fs_ate_10_milhoes

        fs_acumulados = 1 + fs_ate_10_milhoes * 2
        while fs_acumulados > 0:
            if x < 10000000:
                x += 13
                fs_acumulados += 2
            
            x -= 3
            fs_acumulados -= 1
        
        return x

print(f(int(input())))