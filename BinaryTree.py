import Frequence as fr

#Etape 2

class BNode():
    def __init__(self, freq, label=None, leftChild=None, rightChild=None):
        self.freq = freq
        self.label = label
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def getOccurence(self):
        return self.freq
    def getCaractere(self):
        return self.label
    def getLeft(self):
        return self.leftChild
    def getRight(self):
        return self.rightChild


class BTree():
    def __init__(self, document):

        self.document = document

        node_list = [BNode(freq, label) for label, freq in fr.dict_frequences(document).items()]

       

        self.root = node_list[0]

    def get_root(self):
        return self.root

bt = BTree('exemple.txt')
'''
print(bt.get_root().freq)
print(bt.get_root().getRight().getRight().getRight().label)
'''
