Name:           puppet-n1kv_vsm
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        Puppet module for Cisco Nexus1000v VSM
License:        Apache License 2.0

URL:            https://launchpad.net/puppet-n1k-vsm

Source0:        https://github.com/stackforge/puppet-n1k-vsm/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-vswitch
Requires:       puppet >= 2.7.0

%description
Puppet module for Cisco Nexus1000v VSM

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/n1k_vsm/
cp -r %{buildroot}/%{_datadir}/openstack-puppet/modules/n1k_vsm/



%files
%{_datadir}/openstack-puppet/modules/n1k_vsm/


%changelog

