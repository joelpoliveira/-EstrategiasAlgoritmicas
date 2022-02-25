from sys import stdin, stdout


def read_all():
	return stdin.readlines()

def readln():
	return stdin.readline().rstrip()

def outln(n):
	stdout.write(str(n) + "\n")

class Node:
	def __init__(self, int = None, c = None, l = None, r = None, parent = None):
		self.value = int
		self.color = c
		self.left = l
		self.right = r
		self.parent = parent

	def is_leaf(self):
		return (self.left is None) and (self.right is None)

	def get_left_max(self):
		node = self.left
		while node.right:
			node = node.right
		return node

	def __str__(self):
		return f"( {self.value}, {self.color} ), "

class RBTree:
	def __init__(self):
		self.root : Node = None

	def rot_right(self, node):
		p_node = node.parent
		g_node = p_node.parent
		gg_node = g_node.parent

		if gg_node is not None:
			is_left = (gg_node.left == g_node)
			if (is_left):
				gg_node.left = p_node
			else:
				gg_node.right = p_node
		
		g_node.left = p_node.right
		p_node.parent = gg_node
		p_node.right = g_node
		g_node.parent = p_node
		
		p_node.color = 'b'
		g_node.color = 'r'

		if p_node.parent == None:
			self.root = p_node

	def rot_left(self, node):
		p_node = node.parent
		g_node = p_node.parent
		gg_node = g_node.parent

		if gg_node is not None:
			is_left = (gg_node.left == g_node)
			if (is_left):
				gg_node.left = p_node
			else:
				gg_node.right = p_node
		
		g_node.right = p_node.left
		p_node.parent = gg_node
		p_node.left = g_node
		g_node.parent = p_node
		
		p_node.color = 'b'
		g_node.color = 'r'

		if p_node.parent == None:
			self.root = p_node

	def rot_left_right(self, node):
		p_node = node.parent
		g_node = p_node.parent

		is_left = (g_node.left == p_node)
		if is_left:
			g_node.left = node
		else:
			g_node.right = node
		
		p_node.right = node.left
		p_node.parent = node
		node.left = p_node
		node.parent = g_node

		self.rot_right(node.left)
		

	def rot_right_left(self, node):
		p_node = node.parent
		g_node = p_node.parent

		is_left = (g_node.left == p_node)
		if is_left:
			g_node.left = node
		else:
			g_node.rigt = node
		
		p_node.left = node.right
		p_node.parent = node
		node.right = p_node
		node.parent = g_node

		self.rot_left(node.right)

	def check_colors(self, node):
		if (node is None):
			return
		
		if (node == self.root) or (node.parent == self.root):
			return
		
		p_node = node.parent
		if p_node.color == 'b':
			return
			
		g_node = p_node.parent
		if node.color == 'r':
			if node == p_node.right:
				if p_node == g_node.right:
					u_node = g_node.left
					if (u_node is None) or (u_node.color == 'b'):
						self.rot_left(node)
						self.check_colors(node.parent)
					elif u_node.color == 'r':
						u_node.color = 'b'
						p_node.color = 'b'
						g_node.color = 'r'
						self.check_colors(node.parent)

				elif p_node == g_node.left:
					u_node = g_node.right
					if (u_node is None) or (u_node.color == 'b'):
						self.rot_left_right(node)
						self.check_colors(node.parent)
					elif u_node.color == 'r':
						u_node.color = 'b'
						p_node.color = 'b'
						g_node.color = 'r'
						self.check_colors(node.parent)

			elif node == p_node.left:
				if p_node == g_node.left:
					u_node = g_node.right
					if (u_node is None) or (u_node.color == 'b'):
						self.rot_right(node)
						self.check_colors(node.parent)
					elif u_node.color == 'r':
						u_node.color = 'b'
						p_node.color = 'b'
						g_node.color = 'r'
						self.check_colors(node.parent)

				elif p_node == g_node.right:
					u_node = g_node.left
					if (u_node is None) or (u_node.color == 'b'):
						self.rot_right_left(node)
						self.check_colors(node.parent)
					elif u_node.color == 'r':
						u_node.color = 'b'
						p_node.color = 'b'
						g_node.color = 'r'
						self.check_colors(node.parent)
		

	def rb_insert(self, int):
		if self.root is None:
			self.root = Node(int, 'b')
		else:

			node_now = self.root
			while True:
				#self.check_colors(node_now)
				if int < node_now.value:
					if node_now.left is None:
						new_node = Node(int, 'r', None, None, node_now)
						node_now.left = new_node
						break
					node_now = node_now.left
				else:
					if node_now.right is None:
						new_node = Node(int, 'r', None, None, node_now)
						node_now.right = new_node
						break
					node_now = node_now.right
			self.check_colors(new_node)
		self.root.color = 'b'
	
	def rb_find(self, int):
		if self.root is None:
			return None

		node_now = self.root
		while True:
			if (node_now is None) or (int == node_now.value):
				return node_now

			if int < node_now.value:
				node_now = node_now.left

			elif int > node_now.value:
				node_now = node_now.right
		
	def rb_erase(self, int):
		if self.root is None:
			return None
		
		node_now = self.root
		while True:
			if (node_now is None) or (int == node_now.value):
				break
			if int < node_now.value:
				node_now = node_now.left
			elif int > node_now.value:
				node_now = node_now.right
		
		if node_now is None:
			return None 

		if node_now.is_leaf():
			if node_now.color == 'r':
				if node_now.parent.left == node_now:
					node_now.parent.left = None
				else:
					node_now.parent.right = None
				del node_now
			else:
				pass
		elif node_now.left is not None and node_now.left.is_leaf():
			if (node_now.color == 'b') and (node_now.left.color == 'r') or (node_now.color == 'r') and (node_now.left.color == 'b'):
				node_now.color = 'b'
				node_now.value = node_now.left.value
				del node_now.left
				node_now.left = None
			else:
				pass

		elif node_now.right is not None and node_now.right.is_leaf():
			if (node_now.color == 'b') and (node_now.right.color == 'r') or (node_now.color == 'r') and (node_now.right.color == 'b'):
				node_now.color = 'b'
				node_now.value = node_now.right.value
				del node_now.right
				node_now.right = None
			else:
				pass	
		else:
			if node_now.left is not None and node_now.right is not None:
				left_max_node = node_now.get_left_max()
				if left_max_node == left_max_node.parent.left:
					left_max_node.parent.left = None
				else:
					left_max_node.parent.right = None
				
				node_now.value = left_max_node.value
				del left_max_node
			
			else:
				pass


	def __str__(self):
		s = '[ '
		stack = []
		node_now = self.root
		depth = 0

		while True:
			if node_now is not None:
				stack.append((node_now, depth))
				node_now = node_now.left
				depth+=1
			elif stack:
				node_now, depth = stack.pop()
				s+=str(node_now) + f"-- {depth}, "
				node_now = node_now.right
				depth += 1
			else:
				break
		s += ']'
		return s

if __name__ == '__main__':
	
	shoes = RBTree()

	while True:
		command = readln()
		if command:
			command = command.split()
			
			if command[0] == "ADD":
				shoes.rb_insert( int(command[1]) )

			outln(shoes)
		else:
			break
	