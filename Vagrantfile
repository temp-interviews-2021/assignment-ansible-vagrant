Vagrant.require_version ">= 2.2.0"

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/bionic64"
  config.ssh.insert_key = false

  # config.vm.define :LB do |cfg|
  #       cfg.vm.network "forwarded_port", guest: 80, host: 80
  #       cfg.vm.network :private_network, ip: "10.0.0.11"
  #       cfg.vm.provider :virtualbox do |v|
  #           v.name = "LB"
  #       end
  #   end

  config.vm.define :App do |cfg|
        cfg.vm.network :private_network, ip: "10.0.0.21"
        cfg.vm.provider :virtualbox do |v|
            v.name = "App"
        end
    end

  # config.vm.define :DB do |cfg|
  #       cfg.vm.network :private_network, ip: "10.0.0.31"
  #       cfg.vm.provider :virtualbox do |v|
  #           v.name = "DB"
  #       end
  #   end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yaml"
    ansible.become = true
  end
end
