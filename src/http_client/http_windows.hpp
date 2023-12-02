#include <windows.h>
#include <winhttp.h>
#include <iostream>
using namespace std;

HINTERNET initialize_session();
int close_session(HINTERNET *);