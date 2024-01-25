# Modify the Ulimit of the /etc/default/nginx for the server to handle traffic

# Increase the ULIMIT of the nginx server
exec { 'update ULIMIT':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 20000\"/' /etc/default/nginx",
  provider => 'shell',
}

exec { 'nginx-restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
