#include "http_windows.hpp"
using namespace std;

HINTERNET initialize_session()
{
    HINTERNET hSession = WinHttpOpen(L"A WinHTTP Example Program/1.0", 
                                    WINHTTP_ACCESS_TYPE_DEFAULT_PROXY, 
                                    WINHTTP_NO_PROXY_NAME, 
                                    WINHTTP_NO_PROXY_BYPASS, 0);
    return hSession;
}

int close_session(HINTERNET *hSession)
{
    int status = WinHttpCloseHandle(*hSession);
    return status;
}