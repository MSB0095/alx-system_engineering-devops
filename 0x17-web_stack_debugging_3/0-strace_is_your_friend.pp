# 0-strace_is_your_friend.pp
exec { 'fix-apache-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html',
  onlyif  => '/usr/bin/test -d /var/www/html',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Exec['fix-apache-permissions'],
}
