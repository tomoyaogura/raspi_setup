#!/bin/bash
ansible-playbook deploy.yml --private-key=\
~/.ssh/raspi_dad/raspi_dad_id_rsa -K -u pi -i hosts
