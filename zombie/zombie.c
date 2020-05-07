#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>


int main()
{
	int child_pid;
	child_pid=fork();
	if(child_pid>0)
	{
		int status;
		
		printf("hi from parent process: %d\n", child_pid);
		wait(&status);
		//sleep(10);
		printf("bye from parent process: %d\n", child_pid);
	}
	else
	{
		printf("hi from child process: %d\n", child_pid);
		sleep(1);
		printf("bye from child process: %d\n", child_pid);

	}
	return 0;
}
