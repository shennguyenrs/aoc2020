#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int PartOne(string filename) {
    ifstream file;
    file.open(filename);

    int result{0};

    if(file.is_open()){
        string line;
        set<char> container;

        while(getline(file, line)) {
            char c;
            stringstream ss(line);

            if(line.length()!=0) {
                while(ss>>c){
                    container.insert(c);
                }

                if(!file.eof()) continue;
                else {
                    cout << "end of file" << endl;
                }
            }

            // Calculate part one
            result += container.size();
            container.clear();
        }
    }

    file.close();
    return result;
}

int PartTwo(string filename) {
    ifstream file;
    file.open(filename);
    int result{0};

    if(file.is_open()){
        string line;
        int lineCount{0};
        map<char, int> container;
        map<char, int>::iterator itr;

        while(getline(file, line)) {
            char c;
            stringstream ss(line);

            if(line.length()!=0) {
                while(ss>>c){
                    itr = container.find(c);

                    if(itr!=container.end()) {
                        itr->second += 1;
                        continue;
                    }

                    // It not found the key
                    container.insert(make_pair(c, 1));
                }
                
                lineCount+=1;
                if(!file.eof()) continue;
            }

            // When line length is empty
            for(itr=container.begin(); itr!=container.end(); itr++) {
                if(itr->second==lineCount) {
                    result+=1;
                }
            }

            lineCount = 0;
            container.clear();
        }
    }

    file.close();
    return result;
}

int main() {
    string filename = "entries.txt";

    cout << "Part one: " << PartOne(filename) << endl;
    cout << "Part two: " << PartTwo(filename) << endl;

    return 0;
}
