#include <algorithm>
#include <pybind11/pybind11.h>
#include <iostream>
#include <exception>
#include "linear_regression.h"

using namespace std;
namespace py=pybind11;

LinearRegression::LinearRegression() {
}

void LinearRegression::fit(Matrix X, Matrix y) {

	//Asumo X son la matriz de variables
	//Asumo Y es un vector de precios.
	//Disclaimer: Recordar que esto solo funciona para variables númericas, no categoricas (titulo, descripción)

	Matrix Xt = X.transpose();

	Matrix newX = Xt * X;
	Matrix newY = Xt * y;

	_res = newX.ldlt().solve(newY);
	

}

Matrix LinearRegression::predict(Matrix X)
{
    //auto ret = MatrixXd::Zero(X.rows(), 1);

	return (X * _res);
}
