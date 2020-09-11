Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    # Pyenv installation
    git clone https://github.com/pyenv/pyenv.git /home/vagrant/.pyenv
    # Add pyenv environment vars to .profile for use with shh
    echo 'export PYENV_ROOT="/home/vagrant/.pyenv"' >> /home/vagrant/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/vagrant/.profile
    echo 'eval "$(pyenv init -)"' >> /home/vagrant/.profile
    # Add pyenv environment vars for use in this script
    export PYENV_ROOT="/home/vagrant/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    pyenv install 3.7.8
    pyenv global 3.7.8
  end