# Modify the Ulimit of the /etc/default/nginx for the server to handle traffic

# Increase the ULIMIT of the nginx server
exec { 'fix--for-nginx:
	command => '/bin/sed -i "s/15/4096" /etc/default/nginx',
	path => '/usr/local/bin:/bin/',
}

exec { 'nginx-restart':
	command => '/etc/init.d/nginx restart',
	path 	=> '/etc/init.d',
}
