class vector():
	data = None
	rank = 0
	parent = None

	def __init__(self, data, rank):
		self.data = data
		self.rank = rank

	@staticmethod
	def vectorize(x):
		vecs = []
		for v in x:			
			newVertex = vector(v, 0)
			newVertex.parent = newVertex
			vecs.append(newVertex)
		return vecs


class DisjointSet():
	e = []

	def __str__(self):
		ret = "Data\tRank\tParent\n"
		for v in self.e:
			ret += "%s\t%s\t%s\n" % (v.data, v.rank, v.parent.data)
		return ret

	def find(self, x):
		if x.parent != x:
			x.parent = self.find(x.parent)
		return x.parent

	def union(self, x, y):
		rx = self.find(x)
		ry = self.find(y)

		if rx == ry:
			return
		if rx.rank > ry.rank:
			ry.parent = rx
		else:
			rx.parent = ry
			if rx.rank == ry.rank:
				ry.rank += 1

def test():
	x = [1, 2, 3, 4, 5, 6, 7, 8]
	v = vector.vectorize(x)
	d = DisjointSet()
	d.e = v

	d.union(v[0], v[1])
	d.union(v[2], v[3])
	d.union(v[4], v[5])
	d.union(v[6], v[7])

	d.union(v[0], v[3])
	d.union(v[5], v[6])

	d.union(v[3], v[4])

	d.find(v[0])

	print(d)

def test2():
	y = ["A", "B", "C", "D", "E", "F", "G", "H"]
	v = vector.vectorize(y)
	f = DisjointSet()
	f.e = v

	f.union(v[0], v[1])
	f.union(v[3], v[6])
	f.union(v[5], v[6])
	f.union(v[7], v[6])
	f.union(v[1], v[2])
	f.union(v[2], v[6])
	f.union(v[2], v[3])
	f.union(v[0], v[4])

	print(f)

test()
test2()
