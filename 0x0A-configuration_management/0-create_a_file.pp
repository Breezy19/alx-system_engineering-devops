# This puppet file creates a file called school in /tmp folder

file {'/tmp/shcool':
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
