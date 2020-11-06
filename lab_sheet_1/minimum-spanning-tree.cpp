// 19000073
// Lab sheet 1
// Question 02

#include <iostream>
#include <vector>
using namespace std;

class Edge {
    public:
    int from;
    int to;
    int weight;
    bool isBiDirectional;
    Edge(int from, int to, int weight, bool isBiDirectional) {
        this->from = from;
        this->to = to;
        this->weight = weight;
        this->isBiDirectional = isBiDirectional;
    }
    void printEdge() {
        if (isBiDirectional) {
            cout << this->from << " <---(" << this->weight << ")---> " << this->to << endl;
            return;
        }
        cout << this->from << " ---(" << this->weight << ")---> " << this->to << endl;
    }
};

class Graph {
    vector<Edge> edges;
    vector<int> vertices;
    public:
    void insertVertex (int v) {
        vertices.push_back(v);
    }
    void insertEdge (int from, int to, int weight, bool isBiDirectional) {
        Edge newEdge(from, to, weight, isBiDirectional);
        edges.push_back(newEdge);
    }
    void printGraph() {
        cout << "-----------------------" << endl;
        cout << "Graph :" << endl;
        cout << "- Vertices: ";
        for (int i = 0; i < vertices.size(); i++) {
            cout << vertices[i] << " ";
        }
        cout << endl << "- Edges: " << endl;
        for (int i = 0; i < edges.size(); i++) {
            cout << "\t";
            edges[i].printEdge();
        }
        cout << "-----------------------" << endl;
    }
    void findMST () {
        for (int i = 0; i < edges.size(); i++) {
            for (int j = i + 1; j < edges.size(); j++) {
                if (edges[i].weight > edges[j].weight) {
                    Edge temp = edges[i];
                    edges[i] = edges[j];
                    edges[j] = temp;
                }
            }
        }
        vector<Edge> minimumSpanningTree;
        int mstVectors[vertices.size()];
        for (int i = 0; i < vertices.size(); i++) {
            mstVectors[i] = 0;
        }
        for (int i = 0; i < edges.size(); i++) {
            Edge current = edges[i];
            if (mstVectors[current.to] < 2 && mstVectors[current.from] < 2) {
                minimumSpanningTree.push_back(current);
                mstVectors[current.to]++;
                mstVectors[current.from]++;
            }
            bool isOnePresent = false;
            for (int i = 0; i < vertices.size(); i++) {
                if (mstVectors[i] == 1) {
                    isOnePresent = true;
                    break;
                }
            }
            if (!isOnePresent) {
                minimumSpanningTree.pop_back();
                mstVectors[current.to]--;
                mstVectors[current.from]--;
            }
        }
        bool isMSTComplete = true;
        for (int i = 0; i < vertices.size(); i++) {
            if (mstVectors[i] == 0) {
                isMSTComplete = false;
                break;
            }
        }
        if (isMSTComplete) {
            cout << "-----------------------" << endl;
            cout << "Minimum Spanning Tree: " << endl;
            for (int i = 0; i < minimumSpanningTree.size(); i++) {
                cout << "\t";
                minimumSpanningTree[i].printEdge();
            }
            cout << "-----------------------" << endl;
            return;
        }
        cout << "Couldn't find a minimum spanning tree!! Sorry :(" << endl;
    }
};

int main () {
    Graph graph;
    // Inserting vertices
    graph.insertVertex(0);
    graph.insertVertex(1);
    graph.insertVertex(2);
    graph.insertVertex(3);
    graph.insertVertex(4);

    // Inserting edges
    graph.insertEdge(1, 0, 3, true);
    graph.insertEdge(0, 3, 3, true);
    graph.insertEdge(3, 2, 2, true);
    graph.insertEdge(2, 4, 1, true);
    graph.insertEdge(4, 1, 4, true);

    //Display graph
    graph.printGraph();

    //Find mst
    graph.findMST();

    Graph g2;
    g2.insertVertex(0);
    g2.insertVertex(1);
    g2.insertVertex(2);
    g2.insertVertex(3);

    g2.insertEdge(0, 1, 5, true);
    g2.insertEdge(1, 2, 1, true);
    g2.insertEdge(2, 3, 4, true);
    g2.insertEdge(3, 0, 5, true);
    g2.insertEdge(3, 1, 2, true);

    g2.printGraph();
    g2.findMST();

    Graph g3;
    g3.insertVertex(0);
    g3.insertVertex(1);
    g3.insertVertex(2);
    g3.insertVertex(3);
    g3.insertVertex(4);

    g3.insertEdge(0, 1, 1, false);
    g3.insertEdge(0, 2, 2, false);
    g3.insertEdge(0, 3, 7, false);
    g3.insertEdge(1, 2, 5, false);
    g3.insertEdge(1, 4, 9, false);
    g3.insertEdge(2, 4, 10, false);
    g3.insertEdge(2, 3, 3, false);
    g3.insertEdge(3, 4, 4, false);

    g3.printGraph();
    g3.findMST();

    Graph uG;
    uG.insertVertex(0);
    uG.insertVertex(1);
    uG.insertVertex(2);
    uG.insertVertex(3);
    uG.insertVertex(4);
    uG.insertVertex(5);

    uG.insertEdge(1, 3, 2, true);
    uG.insertEdge(3, 4, 2, true);
    uG.insertEdge(4, 5, 6, true);
    uG.insertEdge(3, 2, 4, true);
    uG.insertEdge(2, 1, 1, true);
    uG.insertEdge(2, 0, 3, true);
    uG.insertEdge(0, 1, 4, true);

    uG.printGraph();
    uG.findMST();

    return 0;
}
