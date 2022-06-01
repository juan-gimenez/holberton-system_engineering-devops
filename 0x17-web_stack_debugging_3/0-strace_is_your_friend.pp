#!/usr/bin/env bash
<<<<<<< HEAD
# Apache is returning a 500 error
exec { ' debug ':
       onlyif  => 'test -e /var/www/html/wp-settings.php',
       command => "sudo sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
       path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
=======

exec { ' debug ':
  onlyif  => 'test -e /var/www/html/wp-settings.php',
  command => "sudo sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
>>>>>>> f4a3bb878eaf0a3914205709df41e84f59624ad7
