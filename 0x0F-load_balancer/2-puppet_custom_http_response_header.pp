# This script configure custom http header

exec { 'apt update':
    command  => 'sudo apt update',
    provider => shell,
}

package {'nginx':
    ensure => 'installed',
}

Service {'nginx':
    ensure => 'running',
    enable => true,
}
$hostname = $facts['HOSTNAME']
exec {'sed':
    provider => shell,
    command  => 'sed -i -r "s/^\t}$/\t\tadd_header X-Served-By $hostname;\n\t}/" /etc/nginx/sites-available/default',
    require => Package['nginx'],
    notify  => Service['nginx'],
}
