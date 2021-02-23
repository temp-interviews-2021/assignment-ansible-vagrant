# assignment-ansible-vagrant


A simple deployment which deploys two python apps served via nginx behind haproxy using Vagrant and Ansible.


## To run
	
	git clone https://github.com/temp-interviews-2021/assignment-ansible-vagrant.git
	cd assignment-ansible-vagrant
	vagrant up

Post which the following routes should work:

	http://localhost/xyz
	http://localhost/pqrs
	http://localhost/abc
	http://localhost/mno


<!-- ## TODO: -->
<!-- use variables instead of hardcoded values in paths, etc. -->
<!-- use supervisor to run the apps instead of nohup. -->