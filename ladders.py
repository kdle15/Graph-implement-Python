# Author: Lisa Torrey
# Purpose: find word ladders
# Citations:

from structures.graph import Graph

# Read in the words
words = open("words.txt", "r").read().split()

# Start some sets
vertices = set()
edges = set()
a = dict()

# Make each word a vertex
while len(words) > 0:
    word = words.pop()
    vertices.add(word)
    for k in range(len(word)):
        # s is the list of character in word
        s = list(word)
        # modify s[k]
        s[k] = '*'
        # word1 is the signature class that word might fall in. EX: cold falls in *old, c*ld, co*d, col*
        word1 = "".join(s)
        # a is the dictionary that keeps tracks of all these signature classes
        if (word1 in a):
            #if the class is already exits, add word to the class
            a.get(word1).add(word)
            for other in a[word1]:
                edges.add((other,word))
        else:
            b = {word}
            a[word1] = b

# Construct the graph
graph = Graph(vertices, edges)

# Find word ladders
while True:

    source = input("Source word: ")
    if source not in vertices:
        print("Unknown word:", source, "\n")
        continue

    target = input("Target word: ")
    if target not in vertices:
        print("Unknown word:", target, "\n")
        continue

    parents = graph.bfs(source)
    ladder = Graph.path(target, parents)
    print("Shortest ladder:", ladder, "\n")
