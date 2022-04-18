# task 2 execute command
exec  { 'pkill -f killmenow':
    provider => 'shell'
    }