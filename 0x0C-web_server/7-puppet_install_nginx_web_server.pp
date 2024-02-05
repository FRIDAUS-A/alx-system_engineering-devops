# This scipt install nginx server

package {'nginx':
    ensure => 'installed',
}

file {'put inside the index file':
    ensure  => present,
    path    => '/var/www/html/index.html',
    content => 'Hello World!',
}
exec {'sed':
    provider => shell,
    command  => 'sed -i -r "s/^}$/\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/www.youtube.com\/watch\?v=QH2-TGUlwu4;\n\t}\n}/" /etc/nginx/sites-available/default',
}
Service {'nginx':
    ensure => 'running',
    enable => true,
}
