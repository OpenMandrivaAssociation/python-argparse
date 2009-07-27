%define module	argparse
%define name	python-%{module}
%define version 1.0
%define release %mkrel 1

Summary:	A Python command line parser inspired by optparse
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.zip
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

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.txt doc/*

