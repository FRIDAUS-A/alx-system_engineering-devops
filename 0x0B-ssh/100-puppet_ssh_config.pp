#This script set our configuration file

file {'/etc/ssh/ssh_config':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    content => "Host *\n\tPasswordAuthentification no\n\tIdentityFile ~/.ssh/school\n",
}
