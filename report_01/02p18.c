#include <stdio.h>
#include <math.h>

void initial(double *x, double *y, double *dx, double *xmax)
{
	*x = 1.0;
	*y = 1.0;
	*dx = 0.1;
	*xmax = 2.0;
	return;
}

void euler(double *x, double *y, double dx)
{
	double slope, change;
	slope = 2 * *x;
	change = slope * dx;
	*y += change;
	*x += dx;
	return;
}

main()
{
	int i, n, imax;
	double x, y, dx, xmax;

	initial(&x, &y, &dx, &xmax);
	i = 0;
	imax = xmax / dx;
	printf("%4d %6.3f %6.3f\n", i, x, y);
	while (i < imax)
	{
		euler(&x, &y, dx);
		i++;
		printf("%4d %6.3f %6.3f\n", i, x, y);
	}
}
