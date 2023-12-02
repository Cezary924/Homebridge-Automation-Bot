#if defined(_WIN32)
#include "http_client/http_windows.hpp"
#else
#include "http_client/http_unix.hpp"
#endif

int main()
{
  cout << "Hello World!" << endl;

  HINTERNET hSession = initialize_session();
  cout << hSession << endl;
  cout << close_session(&hSession) << endl;

  return 0;
}
