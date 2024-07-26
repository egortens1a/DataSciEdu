from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
colors = {"red": 0, "blue": 0, "green": 0}
level = 0


def run_tree(r, level):
    if (r.attrib['color']!=''):
        level += 1
        colors[r.attrib['color']] += level
    for i in r:
        run_tree(i, level)

run_tree(root,level)

print(*[colors[i] for i in colors])