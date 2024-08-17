# 2-execute_a_command.pp
exec { 'kill_killmenow'
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
}
