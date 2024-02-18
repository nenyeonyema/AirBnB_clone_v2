# File: 101-setup_web_static.pp

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create necessary directories
file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

# Create a symbolic link to the current release
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static'],
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  require => File['/data/web_static/releases/test'],
}
