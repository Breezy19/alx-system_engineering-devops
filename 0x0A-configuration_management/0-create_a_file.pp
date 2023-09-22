# Using puppet, create a file with below specifications

file {'/tmp/school':
ensure  => 'present',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
