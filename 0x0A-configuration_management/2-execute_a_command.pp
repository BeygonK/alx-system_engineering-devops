# Define an exec resource to kill the process named "killmenow"


exec { 'kill_killmenow_process':
  # Specify the command to kill the process using pkill
  command => '/usr/bin/pkill killmenow',
  # Only run the command if the process exists
  onlyif  => '/usr/bin/pgrep killmenow',
  # Run the command as root
  user    => 'root',
  # Notify if the command changes
}
