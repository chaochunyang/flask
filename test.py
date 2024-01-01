data = []
with open("./data/pvuv.txt") as fin:
    for line in fin:
        line = line[:-1]
        pdate, pv, uv = line.split("\t")
        data.append((pdate, pv, uv))

type(data)