REM build 2
py -m cython main.pyx --embed
gcc -mconsole -DSIZEOF_VOID_P=8 -DMS_WIN64 main.c -I T:\Anaconda3\include -I T:\Anaconda3\lib\site-packages\numpy\core\include -L T:\Anaconda3\libs -lpython37 -o output