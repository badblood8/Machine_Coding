#include<bits/stdc++.h>

class dice_service(){
    public:
    int roll(){
        return rand()%6 +1;
    }
}