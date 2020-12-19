#include <stdio.h>
#include <math.h>

#define IMAX 10000
#define DT 0.001

#define X 0
#define Y 1

void
init_general (double *GM, double *r)
{
  *GM = 4 * M_PI * M_PI;
  *r = 1.0;
}

void
init_variable (double v_half[], double z_n[], double GM, double dt)
{
  z_n[X] = 1.0;
  z_n[Y] = 0.0;
  double vx_0 = 0;
  double vy_0 = sqrt (GM);
  double r = sqrt(pow(z_n[X],2) + pow(z_n[Y],2));
  double ax_0 = -1 * GM * z_n[X] / pow(r, 3);
  double ay_0 = -1 * GM * z_n[Y] / pow(r, 3);
  v_half[X] = vx_0 + 1/2 * ax_0 * dt;
  v_half[Y] = vy_0 + 1/2 * ay_0 * dt;
}

double
return_a (double GM, double x_i, double r)
{
  return -1 * GM * x_i / pow (r, 3);
}

void
AnotherMethod (double v_half[], double z_n[], double GM, double dt)
{
  for (int n = 0; n < 2; n++){
    double r = sqrt(pow(z_n[X], 2) + pow(z_n[Y], 2));
    v_half[n] = v_half[n] + return_a(GM, z_n[n], r) * dt;
    z_n[n] = z_n[n] + v_half[n] * dt;
  }  
}

int
main ()
{

  // 計算上必要だが変更のない変数
  double GM, r;
  init_general (&GM, &r);
  double dt = DT;

  // 計算上必要だが変更される変数
  double v_half[2];
  double z_n[2];
  init_variable (v_half, z_n, GM, dt);

  // カウンタ関連変数
  int i, imax;
  imax = IMAX;

#ifdef DEBUG
  printf ("DEBUG mode \n");
#endif

  double E_per_m = 0.5 * ((v_half[X] * v_half[X]) + (v_half[Y] * v_half[Y])) - GM;
  printf("X,Y,E/m\n");

  for (i = 0; i <= imax; i++)
    {
      AnotherMethod (v_half, z_n, GM, dt);
      E_per_m = 0.5 * ((v_half[X] * v_half[X]) + (v_half[Y] * v_half[Y])) - GM;
      printf ("%f, %f, %f\n",z_n[X], z_n[Y], E_per_m);
    }

  return 0;
}
