//Victor Spini Paranaiba - 11611EMT005

#include <bits/stdc++.h>
#define PI 3.14159265358979323846
#define rad2deg (180/PI)
#define deg2rad (PI/180)
	
using namespace std;

class num_complexo{
	public:
		double argument;
		double real;
		double modulo;
		double imag;

		num_complexo(double real_, double imag_){
			real = real_;
			imag = imag_;
			modulo = sqrt(pow(real,2) + pow(imag,2)); 
			argument = atan(imag/real) * rad2deg;
		};

class operacao{
	public:
		num_complexo soma(num_complexo nc1, num_complexo nc2){
	double real = nc1.real + nc2.real;
	double imag = nc1.imag + nc2.imag;
	return num_complexo(real,imag);
};

		num_complexo sub(num_complexo nc1, num_complexo nc2){
	double real = nc1.real - nc2.real;
	double imag = nc1.imag - nc2.imag;
	return num_complexo(real,imag);
};
		num_complexo mult(num_complexo nc1, num_complexo nc2){
	double real = nc1.real*nc2.real - nc1.imag*nc2.imag;
	double imag = nc1.real*nc2.imag + nc1.imag*nc2.real;
	return num_complexo(real,imag);
};
		num_complexo div(num_complexo nc1, num_complexo nc2){
	operacao operacao;
	
	num_complexo nc2_conj(nc2.real, -nc2.imag);
	num_complexo real1 = operacao.mult(nc1,nc2_conj);
	double den = pow(nc2.real,2) + pow(nc2.imag,2);
	
	return num_complexo(real1.real/den,real1.imag/den);
};

int main() {
	cout << endl;
	operacao operacao;
	
	num_complexo nc1(6,-4);
	num_complexo nc2(4,2);
	
	num_complexo real1 = operacao.soma(nc1,nc2);
	num_complexo real2 = operacao.sub(nc1,nc2);
	num_complexo real3 = operacao.mult(nc1,nc2);
	num_complexo real4 = operacao.div(nc1,nc2);
	
	cout<< "Numero complexo 1 [nc1]: Re = " << nc1.real <<" Im = " << nc1.imag <<" Modulo = "<< nc1.modulo << " Argumento = "<< nc1.argument <<endl;
	cout<< "Numero complexo 2 [nc2]: Re = " << nc2.real <<" Im = " << nc2.imag <<" Modulo = "<< nc2.modulo << " Argumento = "<< nc2.argument <<endl;
	cout<< "nc1 * nc2: Re = " << real3.real <<" Im = " << real3.imag << endl;
	cout<< "nc1 / nc2: Re = " << real4.real <<" Im = " << real4.imag << endl;
	cout<< "nc1 + nc2: Re = " << real1.real <<" Im = " << real1.imag << endl;
	cout<< "nc1 - nc2: Re = " << real2.real <<" Im = " << real2.imag << endl;

	return 0;
}
