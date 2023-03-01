#include <string.h>
#include <iostream>
//#include <sstream>
#include <fstream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
void	send_data(void)
{
	int		sockfd, connfd, len;
	struct sockaddr_in	addr;
	std::string	request("GET / HTTP/1.1\r\n\r\n");
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	bzero(&addr, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(8000);
	inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);
	if (connect(sockfd, (struct sockaddr*) &addr, sizeof(addr)))
		exit(0);
	write(sockfd, request.c_str(), request.size());
}
int	main(void)
{
	/*
	FILE 		*pipe;
	char		str[200];
	pipe = popen("pcsc_scan 2>&1", "r");
	while (fgets(str, 200, pipe))
		std::cout << "XX  : " << str;
		*/
	send_data();
	//pclose(pipe);
}
