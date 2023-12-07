# Install and configure nginx

exec { 'update':
    command => '/user/bin/apt-get update',
}
-> package { 'nginx':
    ensure => installed,
}

file_line {'header_served_by':
    path  => '/etc/nginx/sites-available/default',
    match => '^server {',
    line  => "server {\n\tadd_header X-Served-By \"$(hostnama)\";",
    multiple => false,  
}
-> exec { 'run':
        command => '/user/sbin/service nginx restart',
}
