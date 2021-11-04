def garden(children, rows, seeds):
    child = input("Name of child :")
    pos = (children.index(child.lower()) * 2)
    for i in rows:
        cups = i[pos:pos+2]
        for o, r in seeds.items():
            cups = cups.replace(o, r)
        print ("%s has cups containing %s on the %s row." % (child, cups.strip().replace(" ", " and "),str(rows.index(i)).replace("0", "first").replace("1", "second")))
        
children = ["alice", "bob", "charlie", "david", "eve", "fred", "ginny", "harriet", "ileana", "joseph", "kincaid", "larry"]
rows = ["VRCGVVRVCGGCCGVRGCVCGCGV", "VRCCCGCRRGVCGCRVVCVGCGCV"]
seeds = {"V" : "Violet ", "R" : "Radish ", "C" : "Clover ", "G" : "Grass "}
garden(children, rows, seeds)
