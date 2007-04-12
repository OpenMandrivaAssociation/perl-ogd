%define module  ogd
%define name    perl-%{module}
%define version 0.02
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Ordered global destruction of objects stored in globals
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://search.cpan.org/CPAN/authors/id/E/EL/ELIZABETH/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module adds ordered destruction of objects stored in global variables in
LIFO order during global destruction.

Ordered global destruction is only applicable to objects stored in non-lexical
variables (even if they are in file scope). Apparently Perl destroys all
objects stored file-level lexicals before the first END block is called.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{perl_vendorlib}/ogd.pm
%{_mandir}/*/*

