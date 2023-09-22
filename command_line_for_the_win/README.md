## STFP Instruction

1. First, establish a connection with SFTP server (server address : localhost):

    '''
    sftp username@server_address
    '''

2. Once connected navigate to the directory where you want to upload the files using cd command

3. Use the 'put' command to upload the files
    
    ```
    put /path/to/local/file.jpg /path/to/virtual_machine/file.jpg
    ```

4. Finally, use the 'exit' command to close the SFTP connection:
    
    '''
    exit
    '''
