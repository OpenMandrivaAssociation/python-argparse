%define module argparse
%define name python-%{module}
%define version 0.8.0
%define release %mkrel 2

Summary: a Python command line parser inspired by optparse
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.zip
License: BSD
Group: Development/Python
Url: http://argparse.python-hosting.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel, python-setuptools
BuildArch: noarch

%description
The argparse module is an optparse-inspired command line parser that
improves on optparse by:

* handling both optional and positional arguments
* supporting parsers that dispatch to sub-parsers
* producing more informative usage messages
* supporting actions that consume any number of command-line args
* allowing types and actions to be specified with simple callables 
  instead of hacking class attributes like STORE_ACTIONS or CHECK_METHODS 

as well as including a number of other more minor improvements on the
optparse API.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README.txt

