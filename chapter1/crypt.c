#define _XOPEN_SOURCE

#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{  
      	if(argc!=3)
            return -1;
        
       char *buf =crypt((const char *)argv[1], (const char *)argv[2]);
 	
	printf("head:: %s, crypt: %s\n", argv[2], buf);
        return 0;
}
