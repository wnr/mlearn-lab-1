import monkdata as m
import dtree as d
import drawtree as dt
import random

def infGain(s):
	for x in range(0, 6):
		print "a", x + 1, " ", d.averageGain(s, m.attributes[x])	


def partition(data, fraction):
	ldata = list(data)
	random.shuffle(ldata)
	bp = int(len(ldata) * fraction)
	return ldata[:bp], ldata[bp:]

def prune(t, val):
	bestTree = t
	bestPerf = d.check(t, val)
	found = True

	while(found):
		found = False
		trees = d.allPruned(bestTree)
		for tree in trees:
			perf = d.check(tree, val)
			if(perf >= bestPerf):
				bestTree = tree
				bestPerf = perf
				found = True
	return bestTree




def testPruned(s, test, fraction):
	train, val = partition(s, fraction)
	t = prune(d.buildTree(train, m.attributes), val)	
	return d.check(t, test)

def test(s, test, num):
	results = []

	for x in range(3, 8 + 1):
		f = float(x) / 10

		acc = 0

		for r in range(num):
			acc += testPruned(s, test, f)

		results.append(acc / num)

	return results

print "monk1"
r = test(m.monk1, m.monk1test, 100)
for n in r:
	print n

print "monk3"
r = test(m.monk3, m.monk3test, 100)
for n in r:
	print n


