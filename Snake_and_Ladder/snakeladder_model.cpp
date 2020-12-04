
#include<bits/stdc++.h>


class snake{
    int head,tail;
    public:
    snake(int x,int y){
        head=x;
        tail=y;
    }

    int get_head(){
        return head;
    }

    int get_tail(){
        return tail;
    }
}

class ladder{
    int bottom,top;
    public:
    snake(int x,int y){
        bottom=x;
        top=y;
    }

    int get_bottom(){
        return bottom;
    }

    int get_top(){
        return top;
    }
}

class player{
    string name;
    player(string val){
        name=val;
    }
    string get_name(){
        return name;
    }
}

class snake_and_ladder_board{
    int size;
    vector<snake>snakes;
    vector<ladder>ladders;
    map<string,int>player_pieces;

    public:

    snake_and_ladder_board(int x){
        size=x;
        snakes=vector<snake>;
        ladders=vector<ladder>;
        player_pieces=map<string,int>;
    }

    int get_size(){
        return size;
    }

    void set_snakes(vector<snake>S){
        snakes=S;
    }

    vector<snake> get_snakes(){
        return snakes;
    }

    void set_ladders(vector<snake>L){
        ladders=L;
    }

    vector<snake> get_ladders(){
        return ladders;
    }

    void set_player_pieces(map<string,int>P){
        player_pieces=P;
    }

    map<string,int> get_player_pieces(){
        return player_pieces;
    }    
}

