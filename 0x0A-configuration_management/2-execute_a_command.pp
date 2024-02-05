#Using Puupet, create a manifest that kills a process named killmenow.

exec {' kill the program killmenow':
    command  => '/usr/bin/pkill killmenow',
    provider => shell
}
