%define module	argparse
%define name	python-%{module}
%define version 1.2.1
%define release %mkrel 1

Summary:	A Python command line parser inspired by optparse
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://argparse.googlecode.com/files/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://argparse.python-hosting.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python >= 2.3
BuildRequires:	python-devel >= 2.3, python-setuptools
BuildArch:	noarch

%description
The argparse module makes writing command line tools in Python easy.
Just briefly describe your command line interface and argparse will
take care of the rest, including:

* parsing the arguments and flags from ``sys.argv``
* converting arg strings into objects for your program
* formatting and printing any help messages
* and much more ... 

For those familiar with the optparse module from the Python standard
library, argparse improves on this module in a number of ways,
including:

* handling positional arguments
* supporting sub-commands
* allowing alternative option prefixes like ``+`` and ``/``
* handling zero-or-more and one-or-more style arguments
* producing more informative usage messages
* providing a much simpler interface for custom types and actions

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILE_LIST
%__chmod -R og-w *.txt doc/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt doc/*
%py_puresitedir/*



%changelog
* Thu Apr 21 2011 Lev Givon <lev@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 656496
- Update to 1.2.1.

* Sun Mar 27 2011 Lev Givon <lev@mandriva.org> 1.2-1
+ Revision: 648599
- Update to 1.2.

* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.1-1mdv2011.0
+ Revision: 598174
- update file list

* Mon Mar 01 2010 Lev Givon <lev@mandriva.org> 1.1-1mdv2010.1
+ Revision: 512979
- Update to 1.1.

* Wed Dec 09 2009 Lev Givon <lev@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 475622
- Update to 1.0.1.
  Fix world-writable files.

* Mon Jul 27 2009 Lev Givon <lev@mandriva.org> 1.0-1mdv2010.0
+ Revision: 400533
- Update to 1.0.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.8.0-2mdv2009.1
+ Revision: 323533
- rebuild

* Thu Jul 17 2008 Lev Givon <lev@mandriva.org> 0.8.0-1mdv2009.0
+ Revision: 237814
- import python-argparse


* Thu Jul 17 2008 Lev Givon <lev@mandriva.org> 0.8.0-1mdv2008.1
- Package for Mandriva.
