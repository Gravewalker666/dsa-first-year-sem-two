// 19000073
// Lab Sheet 1
// Question 1 and 2

#include <iostream>
#include <vector>
#include <map>
#include <deque>
using namespace std;

class UndirectedGraph {
    public:
    map<int, deque<int> > vertices;
    void insertVertex (int v) {
        deque<int> n;
        vertices[v] = n;
        cout << "Successfully inserted vertex (" << v << ")" << endl;
    }
    void insertEdge (int v1, int v2) {
        if (vertices.count(v1) == 0) {
            cout << "Couldn't find vertex " << v1 << " in the graph" << endl;
            return;
        }
        if (vertices.count(v2) == 0) {
            cout << "Couldn't find vertex " << v2 << " in the graph" << endl;
            return;
        }
        vertices[v1].push_back(v2);
        vertices[v2].push_back(v1);
        cout << "Successfully inserted edge " << v1 << " --- " << v2 << endl;
    }
    void deleteVertex (int v) {
        if (vertices.count(v) == 0) {
            cout << "Couldn't find vertex " << v << " in the graph" << endl;
            return;
        }
        cout << "Deleting vertex.... ";
        vertices.erase(v);
        for (map<int, deque<int> >::iterator i = vertices.begin(); i != vertices.end(); i++) {
            deque<int> edges = i->second;
            for (int j = 0; j < edges.size(); j++) {
                if (v == edges[j]) {
                    vertices[i->first].erase(vertices[i->first].begin() + j);
                }
            }
        }
        cout << "Succussfully deleted vertex (" << v << ")" << endl;
    }
    void displayGraph () {
        for (map<int, deque<int> >::iterator i = vertices.begin(); i != vertices.end(); i++) {
            cout << "(" << i->first << ") -> { ";
            deque<int> edges = i->second;
            for (int j = 0; j < edges.size(); j++) {
                cout << edges[j] << " ";
            }
            cout << "}" << endl;
        }
    }
    void findPath (int from, int to) {
        deque<int> queue = vertices[from];
        deque<int> path;
        path.push_front(from);
        vector<int> visited;
        while (!queue.empty()) {
            int vertex = queue[0];
            visited.push_back(vertex);
            path.push_front(vertex);
            queue.pop_front();
            if (vertex == to) {
                cout << "Path found from " << from << " to " << to << endl;
                cout << "Path: "; 
                for (int i = 0; i < path.size(); i++){
                    cout << path[path.size() - 1 - i] << " ";   
                }
                cout << endl;
                return;
            }
            // Backtrack indicator
            int addCount = 0;
            for (int i = 0; i < vertices[vertex].size(); i++) {
                bool isVisited = false;
                for (int j = 0; j < visited.size(); j++) {
                    if (vertices[vertex][i] == visited[j]) isVisited = true;
                }
                if (!isVisited) {
                    queue.push_front(vertices[vertex][i]);
                    addCount++;
                }
            }
            // Removing the latest vertex from the path if it's backtracked
            if (addCount == 0) {
                path.pop_front();
            }
        };
        cout << "Couldn't find a path from " << from << " to " << to << endl;
    }
};

class DirectedGraph : public UndirectedGraph {
    public:
    void insertEdge (int v1, int v2) {
        if (vertices.count(v1) == 0) {
            cout << "Couldn't find vertex " << v1 << " in the graph" << endl;
            return;
        }
        if (vertices.count(v2) == 0) {
            cout << "Couldn't find vertex " << v2 << " in the graph" << endl;
            return;
        }
        vertices[v1].push_back(v2);
        cout << "Successfully inserted edge " << v1 << " ---> " << v2 << endl;
    }
};

int main () {
    // Question 01 Graph - Undirected 
    UndirectedGraph uG;
    // Inserting vertices
    uG.insertVertex(1);
    uG.insertVertex(2);
    uG.insertVertex(3);
    uG.insertVertex(4);
    uG.insertVertex(5);
    uG.insertVertex(6);

    // Inserting Edges
    uG.insertEdge(1, 2);
    uG.insertEdge(1, 6);
    uG.insertEdge(2, 6);
    uG.insertEdge(5, 6);
    uG.insertEdge(3, 6);
    uG.insertEdge(4, 6);

    // uG.displayGraph();
    // uG.deleteVertex(6);
    uG.displayGraph();
    uG.findPath(1, 4);
    
    // Question 02 Graph - Directed
    DirectedGraph dG;
    // Inserting vertices
    dG.insertVertex(1);
    dG.insertVertex(2);
    dG.insertVertex(3);
    dG.insertVertex(4);
    dG.insertVertex(5);

    // Inserting Edges
    dG.insertEdge(1, 2);
    dG.insertEdge(5, 1);
    dG.insertEdge(5, 2);
    dG.insertEdge(4, 5);
    dG.insertEdge(4, 2);
    dG.insertEdge(3, 2);
    dG.insertEdge(3, 4);

    dG.displayGraph();
    dG.deleteVertex(1);
    dG.displayGraph();
    dG.findPath(2, 4);
    dG.findPath(4, 2);
    dG.findPath(1, 2);
    dG.findPath(3, 5);

    return 0;
}