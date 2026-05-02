#include<iostream>
using namespace std;

class student{
    public:
    int id;
    string name;
    int age;
    
    student(int id, string name, int age){
        this->id=id;
        this->name= name;
        this->age=age;
        cout<<this->name<<" constructor called"<<endl;

    }
    
    ~student(){
        cout<<this->name<<" deconstructor called"<<endl;
    }
    
    void study(){
        cout<< this->name <<" is studying"<<endl;
    }
};

int main(){
    student s1(513, "Divanshi Goyal",20);
    
    cout<< s1.name<<endl;
    s1.study();
    
    return 0;
}