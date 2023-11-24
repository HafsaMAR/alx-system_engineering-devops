# This manifest creates a file in /tmp/school with the content "I love Puppet"

file { '/tmp/school':
  ensure  => file,
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  }
