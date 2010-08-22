%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	PHP_DocBlockGenerator
Summary:	%{_pearname} - DocBlock Generator
Summary(pl.UTF-8):	%{_pearname} - generator DocBlock
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	4
License:	The BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aef1de207fb0f11df4279a83314e1bc6
URL:		http://pear.php.net/package/PHP_DocBlockGenerator/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Console_Getopt
Requires:	php-pear-PHP_CompatInfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates the file Page block and the DocBlocks for includes, global
variables, functions, parameters, classes, constants, properties and
methods.

Accepts parameters to set the category name, the package name, the
author's name and email, the license, the package link, etc...
Attempts to guess variable and parameters types.

Aligns the DocBlock tags.

Tags are not updated or added to existing DocBlocks but only
realigned.

The package can be run by: calling the "PHP_DocBlockGenerator" class,
or by running the "docblockgen" DOS/Unix command.

Fully tested with phpUnit. Code coverage test close to 100%.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten tworzy blok strony oraz bloki DocBlock dla dołączanych
plików, zmiennych globalnych, funkcji, parametrów, klas, stałych,
składników oraz metod.

Za pomocą parametrów możliwe jest określenie nazwy kategorii, pakietu,
nazwiska oraz adresu e-mail autora, licencji, adresu pakietu itd.
Pakiet próbuje odgadnąć domyślne wartości.

Pakiet ten może także wyrównać istniejące znaczniki DocBlock.

Znaczniki nie są aktualizowane bądź dodawane do istniejących bloków
DocBlock, są tylko wyrównywane.

Z pakietu można skorzystać na dwa sposoby - wywołując klasę
"PHP_DocBlockGenerator", bądź też za pomocą polecenia "docblockgen".

Pakiet został w pełni przetestowany za pomocą phpUnit. Pokrycie kodu
bliskie 100%..

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install {./,$RPM_BUILD_ROOT}%{_bindir}/docblockgen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/PHP_DocBlockGenerator/docs
%attr(755,root,root) %{_bindir}/docblockgen
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/DocBlockGenerator
%{php_pear_dir}/PHP/DocBlockGenerator.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/PHP_DocBlockGenerator
