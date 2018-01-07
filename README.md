# raspi_setup
Ansible playbooks and scripts for setting up raspberry_pi


mkvirtualenv raspi
pip install -r requirements.txt

Update the hosts file with the ansible_host, ansible_port and 
## Verify connect via ssh
ansible -i hosts all -m ping -u


raspi-config enable SSH
raspi-config enable GPIO