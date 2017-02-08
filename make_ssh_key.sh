#!/bin/bash
PI_NAME="raspi_dad"
SSH_KEY_SUFFIX="_id_rsa"
GIT_KEY_SUFFIX="_git_rsa"
PUB=".pub"
HOST_ID="192.168.0.108"

# Create local key to scp over to raspberry pi for future connection
cd ~/.ssh/
mkdir $PI_NAME
cd $PI_NAME
ssh-keygen -t rsa -f $PI_NAME$SSH_KEY_SUFFIX -N ""
echo "Generated new SSH key... now copying into authrozied_key on host"
ssh-copy-id -i $PI_NAME$SSH_KEY_SUFFIX$PUB pi@$HOST_ID
echo "Done copying host into authorized_keys. Now should be ready for ssh"
ssh-keygen -t rsa -f $PI_NAME$GIT_KEY_SUFFIX -N ""
echo "Generated new git key in key_directory"

