# 1-user_limit.pp

exec { 'increase-file-descriptor-limit':
  command => 'echo "holberton soft nofile 4096" >> /etc/security/limits.conf && echo "holberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  unless  => 'grep -q "holberton" /etc/security/limits.conf',
}
