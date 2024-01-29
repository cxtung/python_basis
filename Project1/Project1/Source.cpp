#include <iostream>
using namespace std;
const int MAX = 100;

void NhapMang(int a[], int n)
{
	if (n == 0)	return;
	NhapMang(a, n - 1);
	cout << "\na[" << n - 1 << "]= ";
	cin >> a[n - 1];
}

void XuatMang(const int a[], int n)
{
	if (n == 0)	return;
	XuatMang(a, n - 1);
	cout << a[n - 1] << "\t";
}
void HoanVi(int a, int b) {
	int temp = a;
	a = b;
	b = temp;
}
void sapXepDuongTangAmGiam(int a[], int n)
{
	for (int i = 0; i < n - 1; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (a[j] > 0 && a[i] > 0)
			{
				if (a[j] < a[i])
					HoanVi(a[i], a[j]);
			}
			if (a[j] < 0 && a[i] < 0)
			{
				if (a[j] > a[i])
					HoanVi(a[i], a[j]);
			}
		}
	}
}

int main() {
	int n;
	int a[MAX];

	cout << "\nNhap spt n= "; cin >> n;
	NhapMang(a, n);
	XuatMang(a, n);

	

	cout << "\nMang sau khi sap xep:" << endl;
	sapXepDuongTangAmGiam(a, n);

	return 0;
}