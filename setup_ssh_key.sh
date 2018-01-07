#!/bin/bash

if [[ ${#} != 2 ]]; then
	echo "Usage: setup_ssh_key <pi_name> <pi_ip>"
	exit
fi

PI_NAME=$1
SSH_KEY_SUFFIX="_id_rsa"
HOST_ID=$2
SSH_DIR="$HOME/.ssh"  

KEY_DIRECTORY="$SSH_DIR/$PI_NAME"
if [ ! -d $KEY_DIRECTORY ]; then
	mkdir $KEY_DIRECTORY
fi

SSH_KEY="$KEY_DIRECTORY/$PI_NAME$SSH_KEY_SUFFIX"

if [ ! -f $SSH_KEY ]; then
   ssh-keygen -t rsa -f $SSH_KEY -N ""
else
   echo "File $SSH_KEY exists... skipping key generation."
fi

# Create local key to scp over to raspberry pi for future connection
echo "Now copying into authrozied_key on host"
ssh-copy-id -i $SSH_KEY.pub pi@$HOST_ID
echo "Done copying host into authorized_keys. Now should be ready for ssh"

echo "Make sure to add the ssh_key with 'ssh-add $SSH_KEY'"
