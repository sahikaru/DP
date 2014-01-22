#include<iostream>
using namespace std;

class FlyBehavior {
    public :
        virtual  void fly(void) = 0;
};

class Duck {
    public :
        FlyBehavior *flyBehavior;
        Duck() {}
        ~Duck() {}
        void performfly(void) {
            flyBehavior->fly();
        }
        void Swim(void) {
            cout <<"I am a duck, I can swim \n";
        }
};

class FlyWithWings : public FlyBehavior {
    public :
        void fly(void) {
            cout << "I'm fly with wings\n";
        }

};

class FlyNoWay : public FlyBehavior {
    public :
        void fly(void) {
            cout << "I can't fly \n";
        }
};

class RedHeadDuck : public Duck {
    public :
        RedHeadDuck(FlyBehavior *flyway) {
            flyBehavior = flyway;
        };
        void performfly(void) {
            flyBehavior->fly();
        }
};

class MallardDuck : public Duck {
    public:
        MallardDuck(FlyBehavior *flynoway) {
            flyBehavior = flynoway;
        }
        void performfly(void) {
           flyBehavior->fly();
        }
};
int main(void) {
    //Duck *duck = new Duck(new FlyWithWings() );
    Duck *duck = new Duck();
    duck->Swim();

    Duck *rd = new RedHeadDuck(new FlyWithWings() );
    rd->performfly();

    Duck *md = new MallardDuck(new FlyNoWay() );
    md->performfly();
    return 1;
}
