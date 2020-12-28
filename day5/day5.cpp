#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    ifstream file;
    file.open("entries.txt");

    vector<float> vec;

    float max{0};

    if(file.is_open())
    {
        string line;

        while(getline(file, line))
        {
            stringstream ss(line);

            float top{127};
            float bot{0};
            float rgt{7};
            float lft{0};
            float col{0};
            float row{0};
            char c;

            while(ss>>c)
            {
                if('F'==c)
                {
                    row = floor((top+bot)/2);
                    top = row;
                }

                if('B'==c)
                {
                    row = ceil((top+bot)/2);
                    bot = row;
                }

                if('L'==c)
                {
                    col = floor((rgt+lft)/2);
                    rgt = col;
                }

                if('R'==c)
                {
                    col = ceil((rgt+lft)/2);
                    lft = col;
                }
            }

            float result = row*8 + col;
            vec.push_back(result);
        }
    }

    file.close();

    sort(vec.begin(), vec.end());
    int i;

    for(i=0; i<vec.size(); i++)
    {
        float miss = vec[i+1] - vec[i];
        if(2==miss)
            cout << vec[i];
    }

    return 0;
}
