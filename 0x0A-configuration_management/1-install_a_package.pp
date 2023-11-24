# Install flask Version 2.1.0 from pip3 Using Puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  }