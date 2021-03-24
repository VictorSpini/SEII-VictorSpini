//Victor Spini Paranaiba - 11611EMT005

#include <bits/stdc++.h>
#define PI 3.14159265358979323846
#define rad2deg (180/PI)
#define deg2rad (PI/180)
	
using namespace std;
int disco;
stack<int> p1; // Primeira pilha
stack<int> p2; // Segunda pilha
stack<int> p3; // Terceira pilha
 
//int cont = 0;
 
void start(){
	for(int i = disco; i > 0;){
		p1.push(i);
		i--;
	}  
}
 
void resultado(stack<int> pilha){
	if(!pilha.empty()){
		for(int i = 0; i < disco; i++){
			cout << pilha.top() << endl;
			pilha.pop();
		}
		cout << endl; 
	}
}

void xy(){
	if(p1.empty()){
		p1.push(p2.top()); p2.pop(); cout<<"y --> x"<<endl;
	}else if(p2.empty()){
		p2.push(p1.top()); p1.pop(); cout<<"x --> y"<<endl;
	}else if(p1.top() < p2.top()){  
		p2.push(p1.top()); p1.pop(); cout<<"x --> y"<<endl; 
	}else if(p2.top() < p1.top()){ 
		p1.push(p2.top()); p2.pop(); cout<<"y --> x"<<endl;
	}
}
 
void xz(){
	if(p1.empty()){       
		p1.push(p3.top()); p3.pop(); cout<<"z --> x"<<endl;  
	}else if(p3.empty()){     
		p3.push(p1.top()); p1.pop(); cout<<"x --> z"<<endl;   
	}else if(p1.top() < p3.top()){   
		p3.push(p1.top()); p1.pop(); cout<<"x --> z"<<endl;   
	}else if(p3.top() < p1.top()){
		p1.push(p3.top()); p3.pop(); cout<<"z --> x"<<endl; 
	}  
}
 
void yz(){
	if(p3.empty()){
		p3.push(p2.top()); p2.pop(); cout<<"y --> z"<<endl; 
	} else if(p2.empty()){
		p2.push(p3.top()); p3.pop(); cout<<"z --> y"<<endl; 
	}else if(p3.top() < p2.top()){
		p2.push(p3.top()); p3.pop(); cout<<"z --> y"<<endl; 
	}else if(p2.top() < p3.top()){      
		p3.push(p2.top()); p2.pop(); cout<<"y --> z"<<endl; 
	}   
}
 
int main(int argc, char *argv[]){
	if (argc != 2) {
		std::cout << "Por favor, insira apenas dois argumentos!\n";
		return 1;
	}
	stringstream ss;
	ss << argv[1];
	ss >> disco;
		
	start();

	if(disco % 2 == 0){ // Se o número de discos for par
		while(p3.size() < disco){ // Repetir até que esteja o disco completo
			xy(); // Primeiro Movimento entre os pinos X e Y
			if(p3.size() == disco) break;
			xz(); // Segundo Movimento entre os pinos X e Z
			if(p3.size() == disco) break;
			yz(); // Terceiro Movimento entre os pinos Y e Z
		}
	}else{
		while(p3.size() < disco){ // Repetir até que esteja o disco completo
			xz(); // Primeiro Movimento entre os pinos X e Z
			if(p3.size() == disco) break;
			xy(); // Segundo Movimento entre os pinos X e Y
			if(p3.size() == disco) break;
			yz(); // Terceiro Movimento entre os pinos Y e Z
		}
	}
	cout << endl;
	cout << "O número de discos da pilha x é de " << p1.size() <<endl;
	cout << "O número de discos da pilha y é de " << p2.size() <<endl;
	cout << "O número de discos da pilha z é de " << p3.size() <<endl;
	cout << endl;
	cout <<"Última pilha:" << endl; resultado(p3);
	}
