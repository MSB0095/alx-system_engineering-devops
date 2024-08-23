# 0-the_sky_is_the_limit_not.pp

exec { 'fix--for-nginx':
  command => '/usr/sbin/nginx -s reload',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => 'test -f /etc/nginx/nginx.conf',
}
