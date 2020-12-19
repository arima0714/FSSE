#include <stdio.h>
#include <math.h>

#define IMAX 10000
#define DT 0.001

#define X 0
#define Y 1

void
init (double *GM, double *r)
{
  *GM = 4 * M_PI * M_PI;
  *r = 1.0;
}

void
init_avz (double a[], double v[], double z[], double GM)
{
  a[X] = 0, a[Y] = 0;
  v[X] = 0, v[Y] = sqrt (GM);
  z[X] = 1, z[Y] = 0;
}

void
EulerRichardson (double az_m[], double vz_i[], double z_i[], double dt,
		 double GM, double r)
{
  // double az_i = -1 * GM * *z_i / pow(r, 3);
  // double vz_m = *z_i + az_i * dt / 2.0;
  // double z_m = *z_i + *vz_i * dt / 2.0;

  double az_i[2];
  double vz_m[2];
  double z_m[2];

  for (int n = 0; n < 2; n++)
    {
      az_i[n] = -1 * GM * z_i[n] / pow (r, 3);
      vz_m[n] = vz_i[n] + az_i[n] * dt / 2.0;
      z_m[n] = z_i[n] + vz_i[n] * dt / 2.0;
    }

  double r_m = sqrt (pow (z_m[X], 2) + pow (z_m[Y], 2));

  // *az_m = -1 * GM * z_m / pow(r, 3);
  // *vz_i = *vz_i + *az_m * dt;
  // *z_i = *z_i + vz_m * dt;

  for (int n = 0; n < 2; n++)
    {
      az_m[n] = -1 * GM * z_m[n] / pow (r_m, 3);
      vz_i[n] = vz_i[n] + az_m[n] * dt;
      z_i[n] = z_i[n] + vz_m[n] * dt;
    }
#ifdef DEBUG
  printf ("vx = %f, vy = %f\n", vz_i[X], vz_i[Y]);
  printf ("vxm = %f, vym = %f\n", vz_m[X], vz_m[Y]);
  printf ("x = %f, y = %f\n", z_i[X], z_i[Y]);
#endif
}

int
main ()
{

  // 計算上必要だが変更のない変数
  double GM, r;
  init (&GM, &r);
  double dt = DT;

  // 計算上必要だが変更される変数
  double az_m[2];
  double vz_i[2];
  double z_i[2];

  init_avz (az_m, vz_i, z_i, GM);

  // カウンタ関連変数
  int i, imax;
  imax = IMAX;

#ifdef DEBUG
  printf ("DEBUG mode \n");
#endif
  double E_per_m = 0.5 * ((vz_i[X] * vz_i[X]) + (vz_i[Y] * vz_i[Y])) - GM;
  printf("X,Y,E/m\n");

  for (i = 0; i <= imax; i++)
    {
      EulerRichardson (az_m, vz_i, z_i, dt, GM, r);
      E_per_m = 0.5 * ((vz_i[X] * vz_i[X]) + (vz_i[Y] * vz_i[Y])) - GM;
      printf ("%f, %f, %f\n", z_i[0], z_i[1], E_per_m);
    }

  return 0;
}
