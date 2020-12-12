#include <iostream>
#include <vector>
// Dynamic Array [Length is not fixed]
// Bonus


// std::vector<int> v;
using namespace std;

vector<vector<int>> adj; // ADJ
// vector<int> color;
// [ 0:[hamsaye hash], 1:[], 2:[]  ]

// namespace alireza
// {
//     int max(){}
// }
// Usage: alireza::max()

int main()
{   
    int v; // vertices
    cin >> v;

    int e; // edges
    cin >> e;

    adj.resize(v);
    // color.resize(v);

    // Construct the Graph
    for(int i = 0; i <e; i++)
    {
        int x, y; // 0..(v-1) 0-based
        // x--; y--; // for 1..v 1-based

        // Simple Graph: Self-edge, multiple edges
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    for(int i = 0; i < v; i++)
    {
        cout << i << " [ ";
        // for(int j = 0; j < adj[i].size(); j++)
        // adj[i][j]
        // other(below): j
        for(int j : adj[i])
        {
            cout << j << ", ";
        }

        cout << " ]\n";
    }

    // Next: DFS / BFS
    // PacMan-Agent-Hard: BFS
}



    // vector<int> v;
    // // push_back, pop_back, v[i] 0 1 2
    // v.push_back(1);
    // v.push_back(2);
    // for(int i = 0; i < v.size(); i++)
    //     cout << v[i] << " ";