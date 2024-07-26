from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')
def print_tree(r):
    if (r.text.strip()!=''):
        print(r.text)
    for i in r:
        print_tree(i)
print_tree(root)