# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => 'file',
}

# Ensure the SSH client is configured to use the private key ~/.ssh/school
file_line { 'Set SSH Identity File':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^#?[\s]*IdentityFile\s+~/.ssh/school',
  require => File['/etc/ssh/ssh_config'],
}

# Ensure the SSH client is configured to refuse password authentication
file_line { 'Disable Password Authentication':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  match   => '^#?[\s]*PasswordAuthentication\s+no',
  require => File['/etc/ssh/ssh_config'],
}
