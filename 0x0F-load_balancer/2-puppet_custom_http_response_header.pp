class nginx {
    package { 'nginx':
        ensure => installed,
    }

    service { 'nginx':
    enable  =>true,
    ensure  => running,
    require => [Package['nginx']],
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "server {
                        listen 80 default_server;
                        listen [::]:80 default_server;
                        server_name _;
                        location / {
                            add_header X-Served-By $hostname;
                            root /var/www/html;
                            index index.html index.htm index.nginx-debian.html;
                        }
                    }"
        require => [Package['nginx'], Service['nginx']],
        notify  => Service['nginx'],

    }
}

# the name of the custom HTTP header must be X-served-By

# the value of the custom HTTP header must be the hostname of the server Nginx is running on
