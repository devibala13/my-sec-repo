class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def push(self, item):
        self.stack.append(item)


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def push(self, item):
        self.queue.append(item)


class Graph:
    def __init__(self):
        self.graph = None

    def create_graph(self):
        self.graph = {}
        print("Graph created")

    def add_node(self, node):
        if self.graph is not None:
            if node not in self.graph:
                self.graph[node] = {}
                print("Node added successfully")
            else:
                print("Node already exists")
        else:
            print("Create the graph first")

    def add_edge(self, u, v):
        if self.graph is not None:
            if u in self.graph and v in self.graph:
                self.graph[u][v] = 1
                self.graph[v][u] = 1
                print("Edge added successfully")
            else:
                print("One or both nodes do not exist")
        else:
            print("Graph not created")

    def delete_node(self, node):
        if self.graph is not None:
            if node in self.graph:
                self.graph.pop(node)
                for n in self.graph:
                    if node in self.graph[n]:
                        self.graph[n].pop(node)
                print("Node deleted")
            else:
                print("Node does not exist in the graph")
        else:
            print("Graph not created yet!")

    def delete_edge(self, u, v):
        if self.graph is not None:
            if u in self.graph and v in self.graph[u]:
                self.graph[u].pop(v)
                self.graph[v].pop(u)
                print("Edge deleted")
            else:
                print("Edge does not exist")
        else:
            print("Create the graph first")

    def display_graph(self):
        if self.graph is not None:
            for node in self.graph:
                print(f"{node} ; {self.graph[node]}")
        else:
            print("Graph not created")

    def display_adjacency_list(self, node):
        if self.graph is not None:
            if node in self.graph:
                print(f"{node} : {self.graph[node]}")
            else:
                print("Node does not exist")
        else:
            print("Graph not created")

    def bfs(self, start_node, end_node):
        if self.graph is not None:
            if start_node not in self.graph:
                print("Start node does not exist in the graph")
                return
        else:
            print("Graph is not created")
            return
        
        queue = Queue()
        visited = set()
        queue.push(start_node)
        visited.add(start_node)
        while not queue.is_empty():
            node = queue.pop()
            print(f"{node} ", end=" ")
            if node == end_node:
                return
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.push(neighbor)
                    visited.add(neighbor)
        print()

    def dfs(self, start_node, end_node):
        if self.graph is None:
            print("Graph is not created")
            return

        if start_node not in self.graph:
            print("Start node does not exist in the graph")
            return
        
        stack = Stack()
        visited = set()
        stack.push(start_node)
        
        while not stack.is_empty():
            node = stack.pop()
            if node not in visited:
                print(f"{node} ", end=" ")
                visited.add(node)

                if node == end_node:
                    return
                
                for neighbor in reversed(list(self.graph[node].keys())):
                    if neighbor not in visited:
                        stack.push(neighbor)
        
        print("\nEnd node was not found in the graph.")
        
def main():
    g = None

    while True:
        print("Menu")
        print("1. Create the graph")
        print("2. Add node")
        print("3. Add edge")
        print("4. Delete edge")
        print("5. Delete node")
        print("6. Display adjacency list")
        print("7. Display graph")
        print("8. Perform BFS")
        print("9. Perform DFS")
        print("10. Exit")
        choice = int(input("Enter the choice: "))

        if choice == 1:
            g = Graph()
            g.create_graph()

        elif choice == 2:
            if g is not None and g.graph is not None:
                n = int(input("Enter the number of nodes to add: "))
                for i in range(n):
                    node = input(f"Enter the node to add({i}): ")
                    g.add_node(node)
            else:
                print("Graph not created!")

        elif choice == 3:
            if g is not None and g.graph is not None:
                n = int(input("Enter the number of edges to add: "))
                for i in range(n):
                    u = input(f"Enter the starting node of edge({i}): ")
                    v = input(f"Enter the ending node of edge({i}): ")
                    g.add_edge(u, v)
            else:
                print("Graph not created!")

        elif choice == 4:
            if g is not None and g.graph is not None:
                n = int(input("Enter the number of edges to delete: "))
                for i in range(n):
                    u = input(f"Enter the starting node of edge({i}): ")
                    v = input(f"Enter the ending node of edge({i}): ")
                    g.delete_edge(u, v)
            else:
                print("Graph not created!")

        elif choice == 5:
            if g is not None and g.graph is not None:
                n = int(input("Enter the number of nodes to delete: "))
                for i in range(n):
                    node = input(f"Enter the node to delete({i}): ")
                    g.delete_node(node)
            else:
                print("Graph not created!")

        elif choice == 6:
            if g is not None and g.graph is not None:
                node = input("Enter the node: ")
                g.display_adjacency_list(node)
            else:
                print("Graph not created!")

        elif choice == 7:
            if g is not None and g.graph is not None:
                g.display_graph()
            else:
                print("Graph not created!")

        elif choice == 8:
            if g is not None and g.graph is not None:
                start_node = input("Enter the start node: ")
                end_node = input("Enter the end node: ")
                g.bfs(start_node, end_node)
            else:
                print("Graph not created!")

        elif choice == 9:
            if g is not None and g.graph is not None:
                start_node = input("Enter the start node: ")
                end_node = input("Enter the end node: ")
                g.dfs(start_node, end_node)
            else:
                print("Graph not created!")

        elif choice == 10:
            print("Exiting...........")
            break

        else:
            print("Enter the correct choice!!")

main()
