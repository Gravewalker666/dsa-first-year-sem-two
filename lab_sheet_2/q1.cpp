// 19000073
// Lab sheet 2

#include <iostream>
#include <map>
#include <vector>
#include <deque>
using namespace std;

class Graph {
    public:
    map< char, deque<char> > vertices;    
    void insertVertex (char v) {
        deque<char> newEdges;
        vertices[v] = newEdges;
    }
    void insertEdge (char from, char to) {
        if (vertices.count(from) == 0 || vertices.count(to) == 0) {
            cout << "Couldn't insert vertex make sure the given vertices are in the graph" << endl;
            return;
        }
        vertices[from].push_back(to);
    }
    // Question 01 - Checking if theres a path between two vertices
    bool checkPath (char from, char to) {
        if (vertices.count(from) == 0 || vertices.count(to) == 0) {
            cout << "Couldn't check for paths, make sure the given vertices are in the graph" << endl;
            return false;
        }
        deque<char> vertexQ = vertices[from];
        vector<char> visited;
        while (!vertexQ.empty()) {
            char current = vertexQ.front();
            vertexQ.pop_front();
            visited.push_back(current);
            if (current == to) {
                return true;
            }
            for (int i = 0; i < vertices[current].size(); i++) {
                bool isVisited = false;
                for (int j = 0; j < visited.size(); j++) {
                    if (vertices[current][i] == visited[j]) {
                        isVisited = true;
                        break;
                    }
                }
                if (!isVisited) {
                    vertexQ.push_back(vertices[current][i]);
                }
            }
        }
        return false;
    }
    // Question 02 - Checking if theres a cycle in the graph
    bool checkCycle () {
        for (map< char, deque<char> >::iterator i = vertices.begin(); i != vertices.end(); i++) {
            if (checkPath(i->first, i->first)) return true;
        }
        return false;
    }
    // Question 03 - Counting number of paths between two vertices
    int noOfPaths (char from, char to) {
        if (vertices.count(from) == 0 || vertices.count(to) == 0) {
            cout << "Couldn't check for paths, make sure the given vertices are in the graph" << endl;
            return -1;
        }
        if (this->checkCycle()) {
            cout << "The graph contains a cycle, couldn't count the no of paths" << endl;
            return -1;
        }
        int pathCount = 0;
        deque<char> vertexQ = vertices[from];
        while (!vertexQ.empty()) {
            char current = vertexQ.front();
            vertexQ.pop_front();
            if (current == to) {
                pathCount++;
                continue;
            }
            for (int i = 0; i < vertices[current].size(); i++) {
                vertexQ.push_back(vertices[current][i]);
            }
        }
        return pathCount;
    }
    void displayGraph () {
        for (map<char, deque<char> >::iterator i = vertices.begin(); i != vertices.end(); i++) {
            cout << "(" << i->first << ") -> { ";
            deque<char> edges = i->second;
            for (int j = 0; j < edges.size(); j++) {
                cout << edges[j] << " ";
            }
            cout << "}" << endl;
        }
    }
};

int main () {
    Graph g;
    g.insertVertex('a');
    g.insertVertex('b');
    g.insertVertex('c');
    g.insertVertex('d');
    g.insertVertex('e');

    g.insertEdge('a', 'b');
    g.insertEdge('b', 'c');
    g.insertEdge('c', 'a');
    g.insertEdge('d', 'c');
    g.insertEdge('e', 'd');

    g.displayGraph();
    g.checkPath('e', 'a') ? cout << "Path found from e to a!" << endl : cout << "Path not found" << endl;
    g.checkCycle() ? cout << "Cycle found!" << endl : cout << "Cycle not found" << endl;
    g.noOfPaths('e', 'a');

    Graph g1;
    g1.insertVertex('a');
    g1.insertVertex('b');
    g1.insertVertex('c');
    g1.insertVertex('d');
    g1.insertVertex('e');
    g1.insertVertex('f');
    g1.insertVertex('g');

    g1.insertEdge('a', 'b');
    g1.insertEdge('a', 'c');
    g1.insertEdge('b', 'e');
    g1.insertEdge('c', 'd');
    g1.insertEdge('d', 'e');
    g1.insertEdge('c', 'f');
    g1.insertEdge('f', 'e');
    g1.insertEdge('e', 'g');

    g1.displayGraph();
    g1.checkPath('a', 'g') ? cout << "Path found from a to g!" << endl : cout << "Path not found" << endl;
    g1.checkCycle() ? cout << "Cycle found!" << endl : cout << "Cycle not found" << endl;
    cout << "No of paths from a to g: " << g1.noOfPaths('a', 'g') << endl;

    Graph g2;
    g2.insertVertex('a');
    g2.insertVertex('b');
    g2.insertVertex('c');
    g2.insertVertex('d');
    g2.insertVertex('e');
    g2.insertVertex('f');
    g2.insertVertex('g');

    g2.insertEdge('a', 'b');
    g2.insertEdge('a', 'c');
    g2.insertEdge('b', 'e');
    g2.insertEdge('c', 'd');
    g2.insertEdge('d', 'e');
    g2.insertEdge('f', 'e');
    g2.insertEdge('e', 'g');

    g2.displayGraph();
    g2.checkPath('a', 'g') ? cout << "Path found from a to g!" << endl : cout << "Path not found" << endl;
    g2.checkCycle() ? cout << "Cycle found!" << endl : cout << "Cycle not found" << endl;
    cout << "No of paths from a to g: " << g2.noOfPaths('a', 'g') << endl; 

    return 0;
}