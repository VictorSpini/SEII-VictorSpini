//Victor Spini Paranaiba - 11611EMT005

#include <bits/stdc++.h>
#define PI 3.14159265358979323846
#define rad2deg (180/PI)
#define deg2rad (PI/180)
	
using namespace std;

int main(int argc, char *argv[]) {
	if (argc != 3) {
		std::cout << "Não foi possível obter nome do arquivo, favor entrar com três argumentos!\n";
		return 1;
	}
	
	ifstream in{argv[1]}; 	// Leitura do argumento 1
	remove(argv[2]); 	
	ofstream out{argv[2]};	

	if (!out) {
		std::cerr << "Erro na criação do arquivo de saida" << argv[2] << '\n'; // Não foi criado argumento2 para edição - operação I/O
		return 1;
	}
	Armazenamento temporário de dados para Read/Write
	static constexpr std::size_t buffsize{1024};
	char buffer[buffsize];

	while (in.read(buffer, buffsize)) {
		out.write(buffer, buffsize);
	}
	out.write(buffer, in.gcount());	// Efetuada a cópia dos dados
}
