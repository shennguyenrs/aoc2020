#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int PartOne(ifstream file) {
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
            }

            // Calculate part one
            result += container.size();
            container.clear();
        }
    }
    
    return result;
}

int PartTwo(ifstream file) {
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

    return result;
}

int main() {
    ifstream file;
    file.open("entries.txt");



    return 0;
}