def n_dam(n):
    def kolize(radek, sloupec):
        for i in range(radek):
            if sachovnice[i] == sloupec or radek-i == abs(sachovnice[i]-sloupec):
                return True
        return False

    def gen_n_dam(radek):
        if radek == n:
            vysledek.append(list(sachovnice))
        else:
            for sloupec in range(n):
                if not kolize(radek, sloupec):
                    sachovnice[radek] = sloupec
                    gen_n_dam(radek+1)
    vysledek, sachovnice = [], [ [] for _ in range(n)]
    gen_n_dam(0)
    return vysledek

print(n_dam(3))