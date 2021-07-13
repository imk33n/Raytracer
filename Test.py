import Image
import ImageDraw

def objread(dateiname):
    f = open(dateiname)
    dreiecke = []
    punkte = []
    for line in f:
        l = line.split()
        if "v" in line:
            punkte.append(tuple(map(float, l[1:])))
        elif "f" in line:
            dreiecke.append(tuple(map(lambda x: int(x)-1, l[1:])))
        else:
            raise Exception("bloed")
    print(punkte[:3], dreiecke[:3])
    return (punkte, dreiecke)

MOD_IDX = {
    "xy" : (0, 1),
    "yz" : (1, 2),
    "xz" : (0, 2),
}
def machebild(tup, name="bild", mode="xy"):
    punkte, dreiecke = tup
    if mode == "all":
        machebild(tup, name, "xy")
        machebild(tup, name, "xz")
        machebild(tup, name, "yz")
        return
    im = Image.new("1", (400, 400))
    draw = ImageDraw.Draw(im)
    x, y = MOD_IDX[mode]
    for e in dreiecke:
        f = [(punkte[p][x], punkte[p][y]) for p in e]
        draw.polygon(f, outline=128)


    im.save(name+ "_"+mode+ ".png")

tup = objread("aufg5.obj")
print("x", len(tup))
#machebild(tup, "a5", "all")