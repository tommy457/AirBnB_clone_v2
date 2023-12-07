# Script that sets up your web servers for the deployment of web_static.

exec { 'update':
  command  => 'apt-get update',
  provider => shell,
}
-> exec { 'install nginx':
  command  => 'apt-get -y install nginx',
  provider => shell,
}

-> package { 'nginx':
  ensure => 'installed',
}

-> exec { 'create test file':
  command  => 'mkdir -p /data/web_static/releases/test/',
  provider => shell,
}

-> exec { 'create shared file':
  command  => 'mkdir -p /data/web_static/shared/',
  provider => shell,
}

-> exec { 'testing':
  command  => 'echo "IT WORKS!" > /data/web_static/releases/test/index.html',
  provider => shell,
}

-> exec { 'linking':
  command  => 'ln -sfn /data/web_static/releases/test /data/web_static/current',
  provider => shell,
}

-> exec { 'ownership':
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => shell,
}

-> exec { 'base':
  command  => 'sudo sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"',
  provider => shell,
}

-> exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
