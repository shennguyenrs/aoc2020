#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <regex>

using namespace std;

// Condition key to check valid passport for part one
static vector<pair<string, bool>> conOne
{
    {"byr", false},
    {"iyr", false},
    {"eyr", false},
    {"hgt", false},
    {"hcl", false},
    {"ecl", false},
    {"pid", false},
};

// Condition key to check valid passport for part two
static vector<pair<string, bool>> conTwo
{
    {"byr", false},
    {"iyr", false},
    {"eyr", false},
    {"hgt", false},
    {"hcl", false},
    {"ecl", false},
    {"pid", false},
};

// Vector of validating function
static vector<bool (*)(string)> _functions;

// Colors to check for ecl in part two
static vector<string> colors
{
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
};

bool getResult(vector<pair<string, bool>>* condition)
{
    bool result{true};

    // Get the result for part one
    // and reset the condition key to false
    for(auto itr=condition->begin(); itr!=condition->end(); itr++)
    {
        result &= itr->second;
        itr->second = false;
    }

    return result;
}

/*
 * Part One
 */

void PartOne(string const key)
{
    for(auto itr=conOne.begin(); itr!=conOne.end(); itr++)
    {
        if(key==itr->first) itr->second=true;
    }
}

/*
 * Part Two
 */

bool checkByr(string value)
{
    stringstream ss(value);
    int year{0};

    ss >> year;
    if(year>=1920 && year<=2002) return true;
    return false;
}

bool checkIyr(string value)
{
    stringstream ss(value);
    int year{0};

    ss >> year;
    if(year>=2010 && year<=2020) return true;
    return false;
}

bool checkEyr(string value)
{
    stringstream ss(value);
    int year{0};

    ss >> year;
    if(year>=2020 && year<=2030) return true;
    return false;
}

bool checkHgt(string value)
{
    stringstream ss(value);
    int hgt{0};
    string unit;

    ss >> hgt >> unit;
    
    if("cm"==unit)
    {
        if(hgt>=150 && hgt<=193) return true;
        return false;
    }

    if(hgt>=59 && hgt<=76) return true;
    return false;
}

bool checkHcl(string value)
{
    regex pattern{"^#([a-f]|[0-9]){6}$"};
    return regex_match(value, pattern);
}

bool checkEcl(string value)
{
    for(auto itr=colors.begin(); itr!=colors.end(); itr++)
    {
        if(*itr==value) return true;
    }

    return false;
}

bool checkPid(string value)
{
    regex pattern{"[0-9]{9}$"};
    return regex_match(value, pattern);
}

void addFunctions()
{
    _functions.push_back(checkByr);
    _functions.push_back(checkIyr);
    _functions.push_back(checkEyr);
    _functions.push_back(checkHgt);
    _functions.push_back(checkHcl);
    _functions.push_back(checkEcl);
    _functions.push_back(checkPid);
}

void PartTwo(string const key, string const value)
{
    unsigned int i;

    for(i=0; i<conTwo.size(); i++)
    {
        if(key==conTwo[i].first) 
            conTwo[i].second = _functions[i](value); 
    }
}

/*
 * Main
 */

int main()
{
    ifstream file;
    file.open("entries.txt");

    unsigned int countOne{0};
    unsigned int countTwo{0};

    // Prepare funtions for part two
    addFunctions();

    if(file.is_open())
    {
        string line;

        while(getline(file, line))
        {
            if('\r'!=line[0]) // Or line.length()==1
            {
                stringstream ss(line);
                string check;
                
                while(ss>>check)
                {
                    unsigned int len = check.length();
                    string key = check.substr(0, 3);
                    string value = check.substr(4, len-4);

                    PartOne(key);
                    PartTwo(key, value);
                }

                continue;
            }
            
            // Part one
            if(getResult(&conOne)) countOne++;

            // Part two
            if(getResult(&conTwo)) countTwo++;
        }
    }

    // Close file
    file.close();

    // Print out result
    cout << "Part one: " << countOne << endl;
    cout << "Part two: " << countTwo << endl;

    return 0;
}
