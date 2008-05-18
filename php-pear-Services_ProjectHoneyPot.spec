%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	ProjectHoneyPot
%define		_status		alpha
%define		_pearname	Services_ProjectHoneyPot
Summary:	%{_pearname} - A package to interface the http:bl API of ProjectHoneyPot.org
Summary(pl.UTF-8):	%{_pearname} - interfejs do API http:bl projektu ProjectHoneyPot.org
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e6011e571bac41ba520a53ebb12155f3
URL:		http://pear.php.net/package/Services_ProjectHoneyPot/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Net_CheckIP2 >= 1.0.0RC2
Requires:	php-pear-Net_DNS >= 1.0.0
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is used to determine if an IP or hostname are a) a search
engine, b) suspicious, c) the ip of a harvester or/and d) of a comment
spammer.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten umożliwia określenie czy dany adres IP lub nazwa host to a)
wyszukiwarka internetowa, b) podejrzany adres c) adres ip zbieracza
adresów i/lub d) spammer.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_ProjectHoneyPot/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/ProjectHoneyPot
%{php_pear_dir}/Services/ProjectHoneyPot.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_ProjectHoneyPot
