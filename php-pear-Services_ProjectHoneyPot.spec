%define		status		beta
%define		pearname	Services_ProjectHoneyPot
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A package to interface the http:bl API of ProjectHoneyPot.org
Summary(pl.UTF-8):	%{pearname} - interfejs do API http:bl projektu ProjectHoneyPot.org
Name:		php-pear-%{pearname}
Version:	0.6.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	9dc38df7077f41f93e3e2c992e17e85c
URL:		http://pear.php.net/package/Services_ProjectHoneyPot/
BuildRequires:	php-pear-PEAR >= 1:1.9.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(spl)
Requires:	php-pear
Requires:	php-pear-Net_CheckIP2 >= 1.0.0-0.RC3
Requires:	php-pear-Net_DNS2 >= 1.1.4
Requires:	php-pear-PEAR-core >= 1:1.4.0
Obsoletes:	php-pear-Services_ProjectHoneyPot-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is used to determine if an IP or hostname are a) a search
engine, b) suspicious, c) the ip of a harvester or/and d) of a comment
spammer.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten umożliwia określenie czy dany adres IP lub nazwa host to a)
wyszukiwarka internetowa, b) podejrzany adres c) adres ip zbieracza
adresów i/lub d) spammer.

Ta klasa ma w PEAR status: %{status}.

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
