%define module  ogd

Name:		perl-%{module}
Version:	%perl_convert_version 0.03
Release:	1
Summary:	Ordered global destruction of objects stored in globals
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/E/EL/ELIZABETH/ogd-0.03.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module adds ordered destruction of objects stored in global variables in
LIFO order during global destruction.

Ordered global destruction is only applicable to objects stored in non-lexical
variables (even if they are in file scope). Apparently Perl destroys all
objects stored file-level lexicals before the first END block is called.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%{perl_vendorlib}/ogd.pm
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.02-6mdv2010.0
+ Revision: 430518
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-5mdv2009.0
+ Revision: 241806
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-3mdv2008.0
+ Revision: 86738
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2007.0
- Rebuild

* Thu Mar 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk
- first mdk release


