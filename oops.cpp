#include<iostream>
using namespace std;

class student{
    private:
    int id;
    string name;
    int age;

    
    string gf;

    public:
    // parameterized constructor
    student(int id, string name, int age, string gf){
        this->id=id;
        this->name= name;
        this->age=age;
        cout<<this->name<<" constructor called"<<endl;

    }

    // copy constructor
    student(const student &srcobj){
        this->id=srcobj.id;
        this->name= srcobj.name;
        this->age=srcobj.age;
        cout<<this->name<<" constructor called"<<endl;

    }
    
    ~student(){
        cout<<this->name<<" deconstructor called"<<endl;
    }
    
    void study(){
        cout<< this->name <<" is studying"<<endl;
    }
    void setage(int age){
        this->age=age;
    }
    void getage() const{
        cout<< this->name<<" is "<<this->age<<" years old"<<endl;
    }
    private:
    void secret(){
        cout<<"This is a secret function"<<endl;
    }
};

int main(){
    // static memory allocation
    student s1(513, "Divanshi Goyal",20,"meenu");
    student s2(s1); // or student s2= s1; // copy constructor is called
    s1.getage();
    //cout<< s2.gf<<endl; // error: 'gf' is a private member of 'student'

    // dynamic memory allocation
    student *s3= new student(510, "Dilnaz", 21, "priya");
    s3->getage();
    delete s3;
    
    return 0;
}