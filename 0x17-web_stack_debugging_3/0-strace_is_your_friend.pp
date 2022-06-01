#!/usr/bin/env bash
# Apache is returning a 500 error
exec { ' debug ':
       onlyif  => 'test -e /var/www/html/wp-settings.php',
       command => "sudo sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
       path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
