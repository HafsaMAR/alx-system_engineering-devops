# update a new limit of files

exec { 'increase soft limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'increase hard limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}
